import base64

from odoo import models, fields, api


class WizardReportYear(models.TransientModel):
    _name = 'report.wizard_report_year'
    _inherit = 'jsr.common'
    _path = 'saguapac/saguapac_report_1'

    year = fields.Integer(string='Year')

    def action_wizard_report_year(self):
        result = self._execute_report(year=self.year)
        result_base64 = base64.b64encode(result)
        attachment_id = self.env['ir.attachment'].create(
            {"name": f"saguapa_report.{self.suffix}", "datas": result_base64})
        download_url = f'/web/content/{attachment_id.id}?download=true'
        return {
            "type": "ir.actions.act_url",
            "url": download_url,
            "target": "new"
        }
