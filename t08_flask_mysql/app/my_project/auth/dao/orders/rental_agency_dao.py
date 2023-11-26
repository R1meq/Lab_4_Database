from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import RentalAgency


class RentalAgencyDAO(GeneralDAO):
    """
    Realization of RentalAgency data access layer.
    """
    _domain_type = RentalAgency
