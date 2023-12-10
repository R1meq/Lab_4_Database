import sqlalchemy
from flask import jsonify

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Rent


class RentDAO(GeneralDAO):
    """
    Realization of Rent data access layer.
    """
    _domain_type = Rent

    def average_rent_price(self):
        result = self._session.execute(sqlalchemy.text("CALL AVERAGE_RENT_PRICE();"))
        result = result.scalar()
        return jsonify({"average_price": result})

