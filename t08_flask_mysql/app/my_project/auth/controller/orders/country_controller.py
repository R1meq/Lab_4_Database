from t08_flask_mysql.app.my_project.auth.service import country_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class CountryController(GeneralController):
    """
    Realisation of Client controller
    """
    _service = country_service

    def insert_10_values(self):
        self._service.insert_10_values()