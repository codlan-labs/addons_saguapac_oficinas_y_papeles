import base64

from odoo import models, fields, api


class WizardReportYear(models.TransientModel):
    _name = 'report.wizard_report_year'
    _inherit = 'jsr.common'
    _path = 'saguapac/saguapac_report_1'
    _report_name = 'saguapac_report_year'

    year = fields.Integer(string='Year')

    def transform_value(self, fld):
        if fld == 'year':
            return self.year - 10

        if fld == "partner_id":
            #hago operacion:
            return "algo"

        return super(WizardReportYear,self).transform_value(fld)



    """
    def mapping_fields(self):
        return {
            "year": "YEAR",
        }
    """
