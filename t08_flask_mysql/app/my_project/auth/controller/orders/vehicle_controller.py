from t08_flask_mysql.app.my_project.auth.service import vehicle_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class VehicleController(GeneralController):
    """
    Realisation of Vehicle controller
    """
    _service = vehicle_service
