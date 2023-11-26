from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import City


class CityDAO(GeneralDAO):
    """
    Realization of City data access layer.
    """
    _domain_type = City
