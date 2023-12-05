from t08_flask_mysql.app.my_project.auth.service import client_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class ClientController(GeneralController):
    """
    Realisation of Rent controller
    """
    _service = client_service

    def insert_client(self,first_name, last_name, phone, email, age, driver_license):
        self._service.insert_client(first_name,last_name,phone,email,age,driver_license)