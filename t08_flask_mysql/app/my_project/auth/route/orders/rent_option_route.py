from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import rent_option_controller
from t08_flask_mysql.app.my_project.auth.domain import RentOption

rent_option_bp = Blueprint('rent_option', __name__, url_prefix='/rent_option')

@rent_option_bp.get('')
def get_all_rent_options() -> Response:
    """
    Gets all objects from the rent_option table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(rent_option_controller.find_all()), HTTPStatus.OK)

@rent_option_bp.post('')
def create_rent_option() -> Response:
    """
    Creates a rent_option using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    rent_option = RentOption.create_from_dto(content)
    rent_option_controller.create(rent_option)
    return make_response(jsonify(rent_option.put_into_dto()), HTTPStatus.CREATED)

@rent_option_bp.get('/<int:rent_option_id>')
def get_rent_option(rent_option_id: int) -> Response:
    """
    Gets a rent_option by id.
    :return: Response object
    """
    return make_response(jsonify(rent_option_controller.find_by_id(rent_option_id)), HTTPStatus.OK)

@rent_option_bp.put('/<int:rent_option_id>')
def update_rent_option(rent_option_id: int) -> Response:
    """
    Updates a rent_option by id.
    :return: Response object
    """
    content = request.get_json()
    rent_option = RentOption.create_from_dto(content)
    rent_option_controller.update(rent_option_id, rent_option)
    return make_response("RentOption updated", HTTPStatus.OK)

@rent_option_bp.patch('/<int:rent_option_id>')
def patch_rent_option(rent_option_id: int) -> Response:
    """
    Patches a rent_option by id.
    :return: Response object
    """
    content = request.get_json()
    rent_option_controller.patch(rent_option_id, content)
    return make_response("RentOption updated", HTTPStatus.OK)

@rent_option_bp.delete('/<int:rent_option_id>')
def delete_rent_option(rent_option_id: int) -> Response:
    """
    Deletes a rent_option by id.
    :return: Response object
    """
    rent_option_controller.delete(rent_option_id)
    return make_response("RentOption deleted", HTTPStatus.OK)

@rent_option_bp.get('/insert_values_many_to_many/<int:rent_id>/<int:option_id>')
def insert_into_many_to_many_table(rent_id,option_id):
    rent_option_controller.insert_into_many_to_many_table(rent_id,option_id)
    return make_response("insert values", HTTPStatus.OK)
