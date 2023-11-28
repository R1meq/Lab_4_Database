from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Fine(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = 'fine'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    violation = db.Column(db.String(45), nullable=False)
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    date = db.Column(db.DATE, nullable=False)
    rent_id = db.Column(db.Integer, db.ForeignKey('rent.id'), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    rent = db.relationship("Rent", backref="fine")

    def __repr__(self) -> str:
        return f"Fine(id={self.id}, violation='{self.violation}', amount={self.amount}, " \
               f"date='{self.date}', rent_id={self.rent_id}, status='{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "violation": self.violation,
            "amount": float(self.amount),  # Convert to float for JSON serialization
            "date": str(self.date),  # Convert to string for JSON serialization
            "rent_id": self.rent_id,
            "status": self.status,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Fine:
        """
        Creates a domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Fine(
            violation=dto_dict.get("violation"),
            amount=dto_dict.get("amount"),
            date=dto_dict.get("date"),
            rent_id=dto_dict.get("rent_id"),
            status=dto_dict.get("status"),
        )
        return obj
