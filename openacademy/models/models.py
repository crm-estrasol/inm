from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RfcMayus(models.Model):
    _inherit = 'res.partner'
    
    vat = fields.Char(
        store=True
    )
    
    @api.onchange('vat')
    def validate_form(self):
        if(self.vat):
            self.vat=self.vat.upper()