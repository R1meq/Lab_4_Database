from t08_flask_mysql.app.my_project.auth.dao import city_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class CityService(GeneralService):
    """
    Realization of City service
    """
    _dao = city_dao
