from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Option


class OptionDAO(GeneralDAO):
    """
    Realization of Option data access layer.
    """
    _domain_type = Option