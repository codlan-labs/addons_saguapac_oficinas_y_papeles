from odoo import models, fields, api


class GeneradorDocumentos(models.Model):
    _inherit = ("generador.documentos")

    service = fields.Selection(selection_add=[("google_drive","Google Drive")])

    def render_google_drive(self,vals):
        return "Documento renderizado en Google Drive service"