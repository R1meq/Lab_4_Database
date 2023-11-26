from t08_flask_mysql.app.my_project.auth.service import location_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class LocationController(GeneralController):
    """
    Realisation of Location controller
    """
    _service = location_service
