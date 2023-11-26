from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import RentOption


class RentOptionDAO(GeneralDAO):
    """
    Realization of RentOption data access layer.
    """
    _domain_type = RentOption