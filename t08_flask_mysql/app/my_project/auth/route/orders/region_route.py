from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import region_controller
from t08_flask_mysql.app.my_project.auth.domain import Region

region_bp = Blueprint('region', __name__, url_prefix='/region')

@region_bp.get('')
def get_all_regions() -> Response:
    """
    Gets all objects from the region table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_all()), HTTPStatus.OK)

@region_bp.post('')
def create_region() -> Response:
    """
    Creates a region using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.create(region)
    return make_response(jsonify(region.put_into_dto()), HTTPStatus.CREATED)

@region_bp.get('/<int:region_id>')
def get_region(region_id: int) -> Response:
    """
    Gets a region by id.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_by_id(region_id)), HTTPStatus.OK)

@region_bp.put('/<int:region_id>')
def update_region(region_id: int) -> Response:
    """
    Updates a region by id.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.update(region_id, region)
    return make_response("Region updated", HTTPStatus.OK)

@region_bp.patch('/<int:region_id>')
def patch_region(region_id: int) -> Response:
    """
    Patches a region by id.
    :return: Response object
    """
    content = request.get_json()
    region_controller.patch(region_id, content)
    return make_response("Region updated", HTTPStatus.OK)

@region_bp.delete('/<int:region_id>')
def delete_region(region_id: int) -> Response:
    """
    Deletes a region by id.
    :return: Response object
    """
    region_controller.delete(region_id)
    return make_response("Region deleted", HTTPStatus.OK)
