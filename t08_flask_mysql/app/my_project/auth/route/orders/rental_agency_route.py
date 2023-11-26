from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import rental_agency_controller
from t08_flask_mysql.app.my_project.auth.domain import RentalAgency

rental_agency_bp = Blueprint('rental_agency', __name__, url_prefix='/rental_agency')

@rental_agency_bp.get('')
def get_all_rental_agencies() -> Response:
    """
    Gets all objects from the rental_agency table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(rental_agency_controller.find_all()), HTTPStatus.OK)

@rental_agency_bp.post('')
def create_rental_agency() -> Response:
    """
    Creates a rental_agency using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    rental_agency = RentalAgency.create_from_dto(content)
    rental_agency_controller.create(rental_agency)
    return make_response(jsonify(rental_agency.put_into_dto()), HTTPStatus.CREATED)

@rental_agency_bp.get('/<int:rental_agency_id>')
def get_rental_agency(rental_agency_id: int) -> Response:
    """
    Gets a rental_agency by id.
    :return: Response object
    """
    return make_response(jsonify(rental_agency_controller.find_by_id(rental_agency_id)), HTTPStatus.OK)

@rental_agency_bp.put('/<int:rental_agency_id>')
def update_rental_agency(rental_agency_id: int) -> Response:
    """
    Updates a rental_agency by id.
    :return: Response object
    """
    content = request.get_json()
    rental_agency = RentalAgency.create_from_dto(content)
    rental_agency_controller.update(rental_agency_id, rental_agency)
    return make_response("Rental Agency updated", HTTPStatus.OK)

@rental_agency_bp.patch('/<int:rental_agency_id>')
def patch_rental_agency(rental_agency_id: int) -> Response:
    """
    Patches a rental_agency by id.
    :return: Response object
    """
    content = request.get_json()
    rental_agency_controller.patch(rental_agency_id, content)
    return make_response("Rental Agency updated", HTTPStatus.OK)

@rental_agency_bp.delete('/<int:rental_agency_id>')
def delete_rental_agency(rental_agency_id: int) -> Response:
    """
    Deletes a rental_agency by id.
    :return: Response object
    """
    rental_agency_controller.delete(rental_agency_id)
    return make_response("Rental Agency deleted", HTTPStatus.OK)
