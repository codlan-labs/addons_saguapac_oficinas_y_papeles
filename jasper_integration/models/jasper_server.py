from odoo import models,fields,api

class JasperServer(models.Model):
    _name = 'jasper.server'

    name = fields.Char(string='Name')
    url = fields.Char(string='URL')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')


class JasperServerReport(models.Model):
    _name = 'jasper.server.report'

    name = fields.Char(string='Name')

    jasper_server_id = fields.Many2one('jasper.server', string='Jasper Server')
