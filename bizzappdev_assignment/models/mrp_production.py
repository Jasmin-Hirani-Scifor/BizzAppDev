# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def write(self, vals):
        """ Prevent changing product_qty after confirmation if linked to a Sale Order. """
        for production in self:
            if 'product_qty' in vals and vals['product_qty'] != production.product_qty:
                if production.state == 'confirmed':

                    is_from_sale_order = False

                    if production.origin and production.origin.strip().upper().startswith('S'):
                        is_from_sale_order = True

                    if is_from_sale_order:
                        raise UserError(_(
                            "You cannot change the quantity of the confirmed Manufacturing Order '%s' "
                            "which is linked to a Sale Order."
                        ) % production.name)

        return super(MrpProduction, self).write(vals)
