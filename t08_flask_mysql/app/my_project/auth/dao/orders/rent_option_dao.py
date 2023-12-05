import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import RentOption


class RentOptionDAO(GeneralDAO):
    """
    Realization of RentOption data access layer.
    """
    _domain_type = RentOption

    def insert_into_many_to_many_table(self, rent_id, option_id):
        self._session.execute(sqlalchemy.text("CALL InsertIntoManyToManyTable(:p1, :p2)"),
                              {"p1": rent_id, "p2": option_id})
        self._session.commit()
