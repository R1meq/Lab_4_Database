from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Location


class LocationDAO(GeneralDAO):
    """
    Realization of Location data access layer.
    """
    _domain_type = Location
