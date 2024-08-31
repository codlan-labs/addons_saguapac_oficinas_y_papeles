from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    ficha_personal_doc = fields.Binary(string='Ficha Personal Document')

    def action_report_ficha_personal(self):
        company = self.env.user.company_id
        generador_documentos = company.instance_generador_documentos()
        vals = {
                "templateName": "DATOS PERSONALES DE CONTACTO.docx",
                "outputName": "DATOS PERSONALES DE CONTACTO.pdf",
                "data": {
                    "name": self.name,
                    "lastname": self.name,
                    "email":self.email,
                    "phone":self.phone
                }
            }
        res = generador_documentos.render(vals)
        self.ficha_personal_doc = res

