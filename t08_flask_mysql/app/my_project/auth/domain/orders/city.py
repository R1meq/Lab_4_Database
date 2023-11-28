from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class City(db.Model, IDto):
    """
    Model declaration for the City table.
    """
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)

    # In City model
    region = db.relationship('Region', backref='city')

    def __repr__(self) -> str:
        return f"City(id={self.id}, name='{self.name}', region_id={self.region_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "region_id": self.region_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = City(
            name=dto_dict.get("name"),
            region_id=dto_dict.get("region_id"),
        )
        return obj
