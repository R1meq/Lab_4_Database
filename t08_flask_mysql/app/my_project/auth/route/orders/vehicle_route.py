from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import vehicle_controller
from t08_flask_mysql.app.my_project.auth.domain import Vehicle

vehicle_bp = Blueprint('vehicle', __name__, url_prefix='/vehicle')

@vehicle_bp.get('')
def get_all_vehicles() -> Response:
    """
    Gets all objects from the vehicle table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(vehicle_controller.find_all()), HTTPStatus.OK)

@vehicle_bp.post('')
def create_vehicle() -> Response:
    """
    Creates a vehicle using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    vehicle = Vehicle.create_from_dto(content)
    vehicle_controller.create(vehicle)
    return make_response(jsonify(vehicle.put_into_dto()), HTTPStatus.CREATED)

@vehicle_bp.get('/<int:vehicle_id>')
def get_vehicle(vehicle_id: int) -> Response:
    """
    Gets a vehicle by id.
    :return: Response object
    """
    return make_response(jsonify(vehicle_controller.find_by_id(vehicle_id)), HTTPStatus.OK)

@vehicle_bp.put('/<int:vehicle_id>')
def update_vehicle(vehicle_id: int) -> Response:
    """
    Updates a vehicle by id.
    :return: Response object
    """
    content = request.get_json()
    vehicle = Vehicle.create_from_dto(content)
    vehicle_controller.update(vehicle_id, vehicle)
    return make_response("Vehicle updated", HTTPStatus.OK)

@vehicle_bp.patch('/<int:vehicle_id>')
def patch_vehicle(vehicle_id: int) -> Response:
    """
    Patches a vehicle by id.
    :return: Response object
    """
    content = request.get_json()
    vehicle_controller.patch(vehicle_id, content)
    return make_response("Vehicle updated", HTTPStatus.OK)

@vehicle_bp.delete('/<int:vehicle_id>')
def delete_vehicle(vehicle_id: int) -> Response:
    """
    Deletes a vehicle by id.
    :return: Response object
    """
    vehicle_controller.delete(vehicle_id)
    return make_response("Vehicle deleted", HTTPStatus.OK)
