from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import fine_controller
from t08_flask_mysql.app.my_project.auth.domain import Fine

fine_bp = Blueprint('fine', __name__, url_prefix='/fine')

@fine_bp.get('')
def get_all_fines() -> Response:
    """
    Gets all objects from the fine table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(fine_controller.find_all()), HTTPStatus.OK)

@fine_bp.post('')
def create_fine() -> Response:
    """
    Creates a fine using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    fine = Fine.create_from_dto(content)
    fine_controller.create(fine)
    return make_response(jsonify(fine.put_into_dto()), HTTPStatus.CREATED)

@fine_bp.get('/<int:fine_id>')
def get_fine(fine_id: int) -> Response:
    """
    Gets a fine by id.
    :return: Response object
    """
    return make_response(jsonify(fine_controller.find_by_id(fine_id)), HTTPStatus.OK)

@fine_bp.put('/<int:fine_id>')
def update_fine(fine_id: int) -> Response:
    """
    Updates a fine by id.
    :return: Response object
    """
    content = request.get_json()
    fine = Fine.create_from_dto(content)
    fine_controller.update(fine_id, fine)
    return make_response("Fine updated", HTTPStatus.OK)

@fine_bp.patch('/<int:fine_id>')
def patch_fine(fine_id: int) -> Response:
    """
    Patches a fine by id.
    :return: Response object
    """
    content = request.get_json()
    fine_controller.patch(fine_id, content)
    return make_response("Fine updated", HTTPStatus.OK)

@fine_bp.delete('/<int:fine_id>')
def delete_fine(fine_id: int) -> Response:
    """
    Deletes a fine by id.
    :return: Response object
    """
    fine_controller.delete(fine_id)
    return make_response("Fine deleted", HTTPStatus.OK)
