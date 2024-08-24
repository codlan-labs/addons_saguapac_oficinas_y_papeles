from odoo import models, fields, api


class JsrCommon(models.TransientModel):
    _name = 'jsr.common'
    _path = '/any/path'

    suffix = fields.Selection(selection=[("pdf", "PDF"), ("xlsx", "XLSX")], required=True,default='pdf')

    def _execute_report(self, **kwargs):
        js_instance = self.env["jasper.server"].instance_jasper_server()
        result = js_instance.report_generate(self._path, self.suffix, **kwargs)
        return result
