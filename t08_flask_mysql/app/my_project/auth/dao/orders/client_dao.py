from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Client


class ClientDAO(GeneralDAO):
    """
    Realization of Client data access layer.
    """
    _domain_type = Client
