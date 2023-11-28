from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Location(db.Model, IDto):
    """
    Model declaration for the Location table.
    """
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(45), nullable=False, unique=True)
    zipcode = db.Column(db.String(45), nullable=False, unique=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    rental_agency_id = db.Column(db.Integer, db.ForeignKey('rental_agency.id'), nullable=False)

    # Define relationships
    city = db.relationship('City', backref='location')
    rental_agency = db.relationship('RentalAgency', backref='location')

    def __repr__(self) -> str:
        return f"Location(id={self.id}, street='{self.street}', zipcode='{self.zipcode}', " \
               f"city_id={self.city_id}, rental_agency_id={self.rental_agency_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "street": self.street,
            "zipcode": self.zipcode,
            "city_id": self.city_id,
            "rental_agency_id": self.rental_agency_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Location:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Location(
            street=dto_dict.get("street"),
            zipcode=dto_dict.get("zipcode"),
            city_id=dto_dict.get("city_id"),
            rental_agency_id=dto_dict.get("rental_agency_id")
        )
        return obj
