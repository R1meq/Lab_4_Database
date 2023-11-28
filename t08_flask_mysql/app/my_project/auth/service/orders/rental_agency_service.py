from t08_flask_mysql.app.my_project.auth.dao import rental_agency_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class RentalAgencyService(GeneralService):
    """
    Realization of RentalAgency service
    """
    _dao = rental_agency_dao
