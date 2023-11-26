from t08_flask_mysql.app.my_project.auth.dao import fine_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class FineService(GeneralService):
    """
    Realization of Fine service
    """
    _dao = fine_dao
