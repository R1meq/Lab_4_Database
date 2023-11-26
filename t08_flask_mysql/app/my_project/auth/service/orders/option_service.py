from t08_flask_mysql.app.my_project.auth.dao import option_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class OptionService(GeneralService):
    """
    Realization of Option service
    """
    _dao = option_dao
