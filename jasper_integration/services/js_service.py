import requests
import json
import urllib.parse

URL_AUTH = "{HOST}/jasperserver/rest_v2/login?j_username={USERNAME}&j_password={PASSWORD}"
URL_REPORT = "{HOST}/jasperserver/rest_v2/reports/{PATH}.{SUFFIX}?j_username={USERNAME}&j_password={PASSWORD}&{PARAMETERS}"


class JsService:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def authenticate(self):
        print("Estas autenticado")
        pass

    def report_generate(self, path, suffix, **kwargs):
        PARAMETERS = urllib.parse.urlencode(kwargs)
        url = URL_REPORT.format(HOST=self.host, USERNAME=self.username, PASSWORD=self.password, PATH=path,
                                SUFFIX=suffix, PARAMETERS=PARAMETERS)
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return ""