from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Rent


class RentDAO(GeneralDAO):
    """
    Realization of Rent data access layer.
    """
    _domain_type = Rent