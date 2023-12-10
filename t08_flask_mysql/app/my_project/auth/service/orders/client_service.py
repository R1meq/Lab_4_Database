from t08_flask_mysql.app.my_project.auth.dao import client_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class ClientService(GeneralService):
    """
    Realisation of Client service
    """
    _dao = client_dao

    def insert_client(self,first_name, last_name, phone, email, age, driver_license):
        self._dao.insert_client(first_name,last_name,phone,email,age,driver_license)
