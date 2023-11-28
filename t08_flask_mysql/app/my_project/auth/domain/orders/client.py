from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Client(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    driver_license = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Client(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', " \
               f"phone='{self.phone}', email='{self.email}', age={self.age}, " \
               f"driver_license='{self.driver_license}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "age": self.age,
            "driver_license": self.driver_license,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Client(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            phone=dto_dict.get("phone"),
            email=dto_dict.get("email"),
            age=dto_dict.get("age"),
            driver_license=dto_dict.get("driver_license"),
        )
        return obj
