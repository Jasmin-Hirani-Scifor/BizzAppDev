from odoo import models, fields, api
from odoo.osv import expression

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('is_company', 'name', 'parent_id.name', 'type', 'company_name', 'commercial_company_name', 'ref')
    def _compute_complete_name(self):
        """ Extend computation of complete_name to include [ref] """
        for partner in self:
            name = partner.with_context({})._get_complete_name()
            if partner.ref:
                name = f"{name} [{partner.ref}]"
            partner.complete_name = name.strip()

    @api.depends('complete_name', 'email', 'vat', 'state_id', 'country_id', 'commercial_company_name', 'ref')
    @api.depends_context('show_address', 'partner_show_db_id', 'address_inline', 'show_email', 'show_vat', 'lang')
    def _compute_display_name(self):
        """ Extend computation of display_name to include [ref] """
        super()._compute_display_name()
        for partner in self:
            if partner.ref:
                partner.display_name = f"{partner.display_name} [{partner.ref}]"

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        """ Search partners by name or reference """
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('ref', operator, name)]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&', '!', ('name', operator, name), '!', ('ref', operator, name)]

        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid).name_get()
