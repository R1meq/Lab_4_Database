from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Vehicle


class VehicleDAO(GeneralDAO):
    """
    Realization of Vehicle data access layer.
    """
    _domain_type = Vehicle
