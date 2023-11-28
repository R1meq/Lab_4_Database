from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Region(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    country = db.relationship("Country", backref="region")

    def __repr__(self) -> str:
        return f"Region(id={self.id}, name='{self.name}', country_id={self.country_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "country_id": self.country_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Region:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Region(
            name=dto_dict.get("name"),
            country_id=dto_dict.get("country_id")
        )
        return obj
