from t08_flask_mysql.app.my_project.auth.service import fine_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class FineController(GeneralController):
    """
    Realisation of Fine controller
    """
    _service = fine_service
