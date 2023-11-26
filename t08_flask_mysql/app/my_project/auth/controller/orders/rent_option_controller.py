from t08_flask_mysql.app.my_project.auth.service import rent_option_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class RentOptionController(GeneralController):
    """
    Realisation of RentOption controller
    """
    _service = rent_option_service
