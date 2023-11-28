from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Country


class CountryDAO(GeneralDAO):
    """
    Realization of Country data access layer.
    """
    _domain_type = Country
