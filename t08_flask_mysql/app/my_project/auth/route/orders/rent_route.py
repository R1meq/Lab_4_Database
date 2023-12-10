from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import rent_controller
from t08_flask_mysql.app.my_project.auth.domain import Rent

rent_bp = Blueprint('rent', __name__, url_prefix='/rent')

@rent_bp.get('')
def get_all_rents() -> Response:
    """
    Gets all objects from the rent table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(rent_controller.find_all()), HTTPStatus.OK)

@rent_bp.post('')
def create_rent() -> Response:
    """
    Creates a rent using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    rent = Rent.create_from_dto(content)
    rent_controller.create(rent)
    return make_response(jsonify(rent.put_into_dto()), HTTPStatus.CREATED)

@rent_bp.get('/<int:rent_id>')
def get_rent(rent_id: int) -> Response:
    """
    Gets a rent by id.
    :return: Response object
    """
    return make_response(jsonify(rent_controller.find_by_id(rent_id)), HTTPStatus.OK)

@rent_bp.put('/<int:rent_id>')
def update_rent(rent_id: int) -> Response:
    """
    Updates a rent by id.
    :return: Response object
    """
    content = request.get_json()
    rent = Rent.create_from_dto(content)
    rent_controller.update(rent_id, rent)
    return make_response("Rent updated", HTTPStatus.OK)

@rent_bp.patch('/<int:rent_id>')
def patch_rent(rent_id: int) -> Response:
    """
    Patches a rent by id.
    :return: Response object
    """
    content = request.get_json()
    rent_controller.patch(rent_id, content)
    return make_response("Rent updated", HTTPStatus.OK)

@rent_bp.delete('/<int:rent_id>')
def delete_rent(rent_id: int) -> Response:
    """
    Deletes a rent by id.
    :return: Response object
    """
    rent_controller.delete(rent_id)
    return make_response("Rent deleted", HTTPStatus.OK)

@rent_bp.get('/get_average_price')
def average_rent_price():
    return make_response(rent_controller.average_rent_price(), HTTPStatus.OK)
