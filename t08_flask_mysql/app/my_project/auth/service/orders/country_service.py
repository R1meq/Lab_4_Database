from t08_flask_mysql.app.my_project.auth.dao import country_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class CountryService(GeneralService):
    """
    Realisation of Country service
    """
    _dao = country_dao

    def insert_10_values(self):
        self._dao.insert_10_values()