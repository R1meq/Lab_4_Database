from t08_flask_mysql.app.my_project.auth.service import rental_agency_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class RentalAgencyController(GeneralController):
    """
    Realisation of Rental Agency controller
    """
    _service = rental_agency_service
