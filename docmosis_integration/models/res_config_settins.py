from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    docmosis_api_key = fields.Char(string="API KEY DOCMOSIS")


    @api.model
    def get_values(self):
        res = super(ResConfigSettings,self).get_values()
        res["docmosis_api_key"] = self.env["ir.config_parameter"].sudo().get_param("docmosis_api_key")
        return res

    def set_values(self):
        self.env["ir.config_parameter"].sudo().set_param("docmosis_api_key",self.docmosis_api_key)
        super(ResConfigSettings,self).set_values()
