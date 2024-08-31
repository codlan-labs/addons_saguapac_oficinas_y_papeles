from odoo import models,fields,api
from odoo.odoo.exceptions import UserError


class GeneradorDocumentos(models.Model):
    _name = "generador.documentos"

    service = fields.Selection(selection=[], string="Servicio de Generación de documentos")

    def render(self, vals):
        """El servicio para generar documentos debe implementar este método de forma obligatoria
        Devuelve un base64 del documento
        """
        func_render = getattr(self, f"render_{self.service}", None)
        if func_render:
            result = func_render(vals)
            return result
        else:
            raise UserError(f"No existe el servicio {self.service}")
