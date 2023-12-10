from t08_flask_mysql.app.my_project.auth.service import rent_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class RentController(GeneralController):
    """
    Realisation of Rent controller
    """
    _service = rent_service

    def average_rent_price(self):
        return self._service.average_rent_price()