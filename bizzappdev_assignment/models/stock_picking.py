# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Point 6: Add field to store copied tags
    x_sale_tag_ids = fields.Many2many(
        'crm.tag',
        string='Sale Order Tags',
        help="Tags copied from the source Sale Order.",
        readonly=True,
        copy=False
    )

    def action_done(self):
        res = super(StockPicking, self).action_done()

        for picking in self:
            if picking.picking_type_code == 'outgoing' and picking.sale_id:
                salesperson = picking.sale_id.user_id
                if salesperson and salesperson.partner_id.email:

                    subject = f"Delivery Completed for SO: {picking.sale_id.name}"
                    body_html = f"""
                        <p>Hello {salesperson.name},</p>
                        <p>The delivery for the Sale Order <strong>{picking.sale_id.name}</strong> has been marked as <strong>Done</strong>.</p>
                        <p>Delivery Reference: {picking.name}</p>
                        <p>Customer: {picking.partner_id.name}</p>
                        <p>Delivered on: {picking.date_done}</p>
                    """

                    mail_values = {
                        'subject': subject,
                        'body_html': body_html,
                        'email_to': salesperson.partner_id.email,
                        'model': 'stock.picking',
                        'res_id': picking.id,
                    }
                    mail = self.env['mail.mail'].create(mail_values)
                    mail.send()

        return res
