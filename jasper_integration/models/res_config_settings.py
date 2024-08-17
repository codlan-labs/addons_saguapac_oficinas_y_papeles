from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    jasper_server_id = fields.Many2one("jasper.server", string="Jasper Server")


    @api.model
    def get_values(self):
        res = super(ResConfigSettings,self).get_values()
        res["jasper_server_id"] = int(self.env["ir.config_parameter"].sudo().get_param("jasper_server_id"))
        return res

    def set_values(self):
        self.env["ir.config_parameter"].sudo().set_param("jasper_server_id",self.jasper_server_id.id)
        super(ResConfigSettings,self).set_values()
