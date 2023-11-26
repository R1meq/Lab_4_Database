from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import option_controller
from t08_flask_mysql.app.my_project.auth.domain import Option

option_bp = Blueprint('option', __name__, url_prefix='/option')

@option_bp.get('')
def get_all_options() -> Response:
    """
    Gets all objects from the option table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(option_controller.find_all()), HTTPStatus.OK)

@option_bp.post('')
def create_option() -> Response:
    """
    Creates an option using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    option = Option.create_from_dto(content)
    option_controller.create(option)
    return make_response(jsonify(option.put_into_dto()), HTTPStatus.CREATED)

@option_bp.get('/<int:option_id>')
def get_option(option_id: int) -> Response:
    """
    Gets an option by id.
    :return: Response object
    """
    return make_response(jsonify(option_controller.find_by_id(option_id)), HTTPStatus.OK)

@option_bp.put('/<int:option_id>')
def update_option(option_id: int) -> Response:
    """
    Updates an option by id.
    :return: Response object
    """
    content = request.get_json()
    option = Option.create_from_dto(content)
    option_controller.update(option_id, option)
    return make_response("Option updated", HTTPStatus.OK)

@option_bp.patch('/<int:option_id>')
def patch_option(option_id: int) -> Response:
    """
    Patches an option by id.
    :return: Response object
    """
    content = request.get_json()
    option_controller.patch(option_id, content)
    return make_response("Option updated", HTTPStatus.OK)

@option_bp.delete('/<int:option_id>')
def delete_option(option_id: int) -> Response:
    """
    Deletes an option by id.
    :return: Response object
    """
    option_controller.delete(option_id)
    return make_response("Option deleted", HTTPStatus.OK)
