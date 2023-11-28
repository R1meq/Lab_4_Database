from t08_flask_mysql.app.my_project.auth.dao import rent_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class RentService(GeneralService):
    """
    Realisation of Rent service
    """
    _dao = rent_dao
