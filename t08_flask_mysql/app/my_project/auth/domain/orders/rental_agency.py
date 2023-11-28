from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class RentalAgency(db.Model, IDto):
    """
    Model declaration for Rental Agency.
    """
    __tablename__ = 'rental_agency'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rental_agency_head = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(20), nullable=False)


    def __repr__(self) -> str:
        return f"RentalAgency(id={self.id}, rental_agency_head='{self.rental_agency_head}', phone='{self.phone}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "rental_agency_head": self.rental_agency_head,
            "phone": self.phone,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RentalAgency:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RentalAgency(
            rental_agency_head=dto_dict.get("rental_agency_head"),
            phone=dto_dict.get("phone")
        )
        return obj
