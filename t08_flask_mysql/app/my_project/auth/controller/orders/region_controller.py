from t08_flask_mysql.app.my_project.auth.service import region_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class RegionController(GeneralController):
    """
    Realisation of Region controller
    """
    _service = region_service
