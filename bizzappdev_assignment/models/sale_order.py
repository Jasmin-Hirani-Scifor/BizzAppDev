# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Point 6: Copy tags to Delivery Orders created from Sale Order
    def _prepare_picking_values(self, partner, picking_vals, direct_delivery):
        values = super()._prepare_picking_values(partner, picking_vals, direct_delivery)

        if not isinstance(values, dict):
            values = {}

        if self.tag_ids:
            values['x_sale_tag_ids'] = [(6, 0, self.tag_ids.ids)]

        return values
