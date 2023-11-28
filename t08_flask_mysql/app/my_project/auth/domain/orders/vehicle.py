from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Vehicle(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(35), nullable=False)
    brand = db.Column(db.String(35), nullable=False)
    gearbox = db.Column(db.String(35), nullable=False)
    seater = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(35), nullable=False)

    def __repr__(self) -> str:
        return f"Vehicle(id={self.id}, name='{self.name}', type='{self.type}', " \
               f"brand='{self.brand}', gearbox='{self.gearbox}', seater={self.seater}, " \
               f"status='{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "brand": self.brand,
            "gearbox": self.gearbox,
            "seater": self.seater,
            "status": self.status,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Vehicle:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Vehicle(
            name=dto_dict.get("name"),
            type=dto_dict.get("type"),
            brand=dto_dict.get("brand"),
            gearbox=dto_dict.get("gearbox"),
            seater=dto_dict.get("seater"),
            status=dto_dict.get("status"),
        )
        return obj
