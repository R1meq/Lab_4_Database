from t08_flask_mysql.app.my_project.auth.dao import location_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class LocationService(GeneralService):
    """
    Realization of Location service
    """
    _dao = location_dao
