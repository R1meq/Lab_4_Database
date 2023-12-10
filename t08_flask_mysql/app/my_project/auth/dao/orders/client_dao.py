import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Client


class ClientDAO(GeneralDAO):
    """
    Realization of Client data access layer.
    """
    _domain_type = Client

    def insert_client(self, first_name, last_name, phone, email, age, driver_license):
        self._session.execute(sqlalchemy.text("CALL InsertValueIntoClient(:p1, :p2, :p3, :p4, :p5, :p6)"),
            {
                "p1": first_name,
                "p2": last_name,
                "p3": phone,
                "p4": email,
                "p5": age,
                "p6": driver_license,
            }
        )
        self._session.commit()