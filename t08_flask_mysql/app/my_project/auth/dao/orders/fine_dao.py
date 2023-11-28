from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Fine


class FineDAO(GeneralDAO):
    """
    Realization of Fine data access layer.
    """
    _domain_type = Fine