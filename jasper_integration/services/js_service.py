
class JsService:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def authenticate(self):
        print("Estas autenticado")
        pass

    def get_reports(self,filter):
        return []