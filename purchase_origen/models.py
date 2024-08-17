from odoo import models,fields
from odoo.exceptions import UserError
class PurchaseOrigin(models.Model):
    _name = "purchase.origin"
    name = fields.Char(string="Name",unique=True)
    date = fields.Datetime(string="Date")
    partner_id = fields.Many2one("res.partner", string="Partner ID")

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    origin_id = fields.Many2one("purchase.origin", string="Origin")

    def button_confirm(self):
        if self.origin_id.exists():
            res = super(PurchaseOrder,self).button_confirm()
        else:
            raise UserError("El origen es obligatorio para confirmar la venta")
        return True

    def _prepare_invoice(self):
        vals = super(PurchaseOrder,self)._prepare_invoice()
        if self.origin_id.exists():
            vals.update(ref=self.origin_id.name)
        return vals
