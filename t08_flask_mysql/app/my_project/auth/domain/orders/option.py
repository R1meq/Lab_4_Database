from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Option(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'option'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(45), nullable=False)
    price = db.Column(db.DECIMAL(8, 2), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

    vehicle = db.relationship("Vehicle", backref="option")

    def __repr__(self) -> str:
        return f"Option(id={self.id}, name='{self.name}', description='{self.description}', " \
               f"price={self.price}, vehicle_id={self.vehicle_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": float(self.price),  # Convert to float for JSON serialization
            "vehicle_id": self.vehicle_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Option:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Option(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            price=dto_dict.get("price"),
            vehicle_id=dto_dict.get("vehicle_id")
        )
        return obj
