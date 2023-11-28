from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Rent(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'rent'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    total_price = db.Column(db.DECIMAL(8, 2), nullable=False)
    pick_up_date = db.Column(db.DATE, nullable=False)
    return_date = db.Column(db.DATE, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

    # Define relationships
    client = db.relationship('Client', backref='rent')
    location = db.relationship('Location', backref='rent')
    vehicle = db.relationship('Vehicle', backref='rent')

    def __repr__(self) -> str:
        return f"Rent(id={self.id}, client_id={self.client_id}, total_price={self.total_price}, " \
               f"pick_up_date='{self.pick_up_date}', return_date='{self.return_date}', " \
               f"location_id={self.location_id}, vehicle_id={self.vehicle_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "client_id": self.client_id,
            "total_price": float(self.total_price),
            "pick_up_date": str(self.pick_up_date),
            "return_date": str(self.return_date),
            "location_id": self.location_id,
            "vehicle_id": self.vehicle_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Rent:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Rent(
            client_id=dto_dict.get("client_id"),
            total_price=dto_dict.get("total_price"),
            pick_up_date=dto_dict.get("pick_up_date"),
            return_date=dto_dict.get("return_date"),
            location_id=dto_dict.get("location_id"),
            vehicle_id=dto_dict.get("vehicle_id"),
        )
        return obj
