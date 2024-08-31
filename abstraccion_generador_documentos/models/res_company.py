from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_options(self):
        return [(option.value, option.name) for option in self.env.ref("abstraccion_generador_documentos.field_generador_documentos__service").selection_ids]

    service = fields.Selection(selection=_get_options, string="Servicio de Generación de documentos")


    def instance_generador_documentos(self):
        return self.env["generador.documentos"].search([("service","=",self.service)],limit=1)