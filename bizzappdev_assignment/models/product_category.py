from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.constrains('name')
    def _check_unique_name(self):
        for category in self:
            existing = self.search([
                ('name', '=', category.name),
                ('id', '!=', category.id)
            ], limit=1)
            if existing:
                raise ValidationError('Product Category name must be unique!')
