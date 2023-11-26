from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Region


class RegionDAO(GeneralDAO):
    """
    Realization of Region data access layer.
    """
    _domain_type = Region
