from t08_flask_mysql.app.my_project.auth.service import rent_option_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class RentOptionController(GeneralController):
    """
    Realisation of RentOption controller
    """
    _service = rent_option_service

    def insert_into_many_to_many_table(self,rent_id,option_id):
        self._service.insert_into_many_to_many_table(rent_id,option_id)