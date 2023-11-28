from t08_flask_mysql.app.my_project.auth.service import option_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class OptionController(GeneralController):
    """
    Realisation of Option controller
    """
    _service = option_service
