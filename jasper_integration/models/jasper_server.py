from odoo import models,fields,api
from odoo.addons.jasper_integration.services.js_service import JsService
class JasperServer(models.Model):
    _name = 'jasper.server'

    name = fields.Char(string='Name')
    url = fields.Char(string='URL')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')


    @api.model
    def instance_jasper_server(self):
        #Objeto que tiene los metodos para llamar a los servicios rest
        jasper_server_id = int(self.env["ir.config_parameter"].sudo().get_param('jasper_server_id'))
        jasper_server = self.browse(jasper_server_id)
        username = jasper_server.username
        password = jasper_server.password
        instance = JsService(username,password)
        instance.authenticate()
        return instance

class JasperServerReport(models.Model):
    _name = 'jasper.server.report'

    name = fields.Char(string='Name')

    jasper_server_id = fields.Many2one('jasper.server', string='Jasper Server')
