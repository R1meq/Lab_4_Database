from t08_flask_mysql.app.my_project.auth.dao import region_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class RegionService(GeneralService):
    """
    Realization of Region service
    """
    _dao = region_dao
