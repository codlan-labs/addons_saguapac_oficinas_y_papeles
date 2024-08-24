from odoo import models, fields, api
import base64
from odoo.http import request


class JsrCommon(models.TransientModel):
    _name = 'jsr.common'
    _path = '/any/path'
    _report_name = 'report_default'

    suffix = fields.Selection(selection=[("pdf", "PDF"), ("xlsx", "XLSX")], required=True, default='pdf')
    report_file = fields.Binary(string='Reporte')

    def _execute_report(self, **kwargs):
        js_instance = self.env["jasper.server"].instance_jasper_server()
        result = js_instance.report_generate(self._path, self.suffix, **kwargs)
        return result

    def get_ignore_fields(self):
        return ["id", "suffix", "display_name", "create_uid", "create_date", "write_uid", "write_date"]

    def mapping_fields(self):
        return {}

    def transform_value(self, fld):
        return self[fld]

    def action_execute_report(self):
        fields = [fld for fld in self._fields if fld not in self.get_ignore_fields()]
        kwargs = {self.mapping_fields().get(fld, fld): self.transform_value(fld) for fld in fields}
        result = self._execute_report(**kwargs)
        result_base64 = base64.b64encode(result)
        self.report_file = result_base64
        download_url = f'/web/content/{self._name}/{self.id}/report_file/{self._report_name}.{self.suffix}?download=true'
        return {
            "type": "ir.actions.act_url",
            "url": download_url,
            "target": "new"
        }


    """
    def action_execute_report_v1(self):
        fields = [fld for fld in self._fields if fld not in self.get_ignore_fields()]
        kwargs = {self.mapping_fields().get(fld, fld): self[fld] for fld in fields}
        result = self._execute_report(**kwargs)
        result_base64 = base64.b64encode(result)
        attachment_id = self.env['ir.attachment'].create(
            {"name": f"{self._report_name}.{self.suffix}", "datas": result_base64})
        download_url = f'/web/content/{attachment_id.id}?download=true'
        return {
            "type": "ir.actions.act_url",
            "url": download_url,
            "target": "new"
        }
    """