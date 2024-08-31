from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    service = fields.Selection(related="company_id.service", readonly=False, string="Servicio de Generación de documentos")
