from t08_flask_mysql.app.my_project.auth.dao import rent_option_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class RentOptionService(GeneralService):
    """
    Realization of RentOption service
    """
    _dao = rent_option_dao
