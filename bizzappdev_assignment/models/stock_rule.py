# -*- coding: utf-8 -*-
import logging
from collections import defaultdict
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class StockRule(models.Model):
    _inherit = 'stock.rule'

    @api.model
    def _run_buy(self, procurements):
        """ Group procurements by (supplier, product category, company) and create Purchase Orders """
        PurchaseOrder = self.env['purchase.order']
        PurchaseOrderLine = self.env['purchase.order.line']
        procurements_by_supplier_category = defaultdict(list)

        # Step 1: Group procurements
        for procurement, rule in procurements:
            supplier = self._get_supplier(procurement)
            if not supplier:
                msg = _('Cannot find a vendor for product %s.') % (procurement.product_id.display_name,)
                self.env['procurement.group']._log_next_activity(procurement, rule, msg)
                continue
            category_id = procurement.product_id.categ_id.id or 0
            grouping_key = (supplier.id, category_id, procurement.company_id.id)
            procurements_by_supplier_category[grouping_key].append((procurement, rule))

        results = []

        # Step 2: Process each group
        for (supplier_id, category_id, company_id), group_procurements in procurements_by_supplier_category.items():
            supplier = self.env['res.partner'].browse(supplier_id)
            company = self.env['res.company'].browse(company_id)

            first_procurement, first_rule = group_procurements[0]

            try:
                po_vals = first_rule._prepare_purchase_order(
                    first_procurement.product_id, first_procurement.product_qty,
                    first_procurement.product_uom, company_id, supplier, first_procurement
                )
                # Safely build the origin
                origin = (po_vals.get('origin') or '')
                origin_suffix = f" [Category:{category_id}]"
                po_vals['origin'] = (origin + origin_suffix).strip()

                # Create the Purchase Order
                po = PurchaseOrder.with_company(company).create(po_vals)
                _logger.info("Created new PO %s for supplier %s (Category ID %s)", po.name, supplier.name, category_id)

            except UserError as e:
                _logger.error("Failed to create PO for supplier %s (Category %s): %s", supplier.name, category_id,
                              str(e))
                self.env['procurement.group']._log_next_activity(first_procurement, first_rule, str(e))
                continue

            # Step 3: Create PO Lines
            errors = []
            for procurement, rule in group_procurements:
                try:
                    line_vals = rule._prepare_purchase_order_line(
                        procurement.product_id, procurement.product_qty,
                        procurement.product_uom, company_id, supplier, po
                    )
                    PurchaseOrderLine.create(line_vals)
                    _logger.debug("Added PO line for %s on PO %s", procurement.product_id.display_name, po.name)

                except UserError as e:
                    _logger.error("Failed to create PO line for product %s: %s", procurement.product_id.display_name,
                                  str(e))
                    self.env['procurement.group']._log_next_activity(procurement, rule, str(e))
                    errors.append(str(e))

            results.append(True)

        return all(results)
