from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.option import Option
from t08_flask_mysql.app.my_project.auth.domain.orders.rent import Rent

class RentOption(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'rent_option'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    rent_id = db.Column(db.Integer, db.ForeignKey('rent.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)

    rent = db.relationship("Rent", backref="rent_option")
    option = db.relationship("Option", backref="rent_option")

    def __repr__(self) -> str:
        return f"RentOption(rent_id={self.rent_id}, option_id={self.option_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            ""
            "id": self.id,
            "rent": Rent.put_into_dto(self.rent),
            "option": Option.put_into_dto(self.option)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RentOption:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RentOption(
            rent_id=dto_dict.get("rent_id"),
            option_id=dto_dict.get("option_id"),
        )
        return obj

