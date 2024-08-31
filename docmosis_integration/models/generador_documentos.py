from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import json
import base64
URL_DOCMOSIS_RENDER = "https://us1.dws4.docmosis.com/api/render"


class GeneradorDocumentos(models.Model):
    _inherit = "generador.documentos"

    service = fields.Selection(selection_add=[("docmosis","Docmosis")])

    def render_docmosis(self,vals):
        if "templateName" not in vals:
            raise UserError("No ha definido el nombre de la plantilla del documento")

        if "outputName" not in vals:
            raise UserError("No ha definido el nombre de salida del documento")

        if "data" not in vals:
            raise UserError("No ha definido los valores para la plantill<")

        docmosis_api_key = self.env["ir.config_parameter"].sudo().get_param("docmosis_api_key")
        vals.update(accessKey=docmosis_api_key)
        # Encabezados
        headers = {
            "Content-Type": "application/json",
        }

        # Realizar la solicitud POST a la API de Docmosis
        response = requests.post(URL_DOCMOSIS_RENDER, data=json.dumps(vals), headers=headers)
        return base64.b64encode(response.content).decode('utf-8')

        #return "Documento renderizado en docmosis service"