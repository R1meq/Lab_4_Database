from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import client_controller
from t08_flask_mysql.app.my_project.auth.domain import Client

client_bp = Blueprint('client', __name__, url_prefix='/client')

@client_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from the client table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)

@client_bp.post('')
def create_client() -> Response:
    """
    Creates a client using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.create(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED)

@client_bp.get('/<int:client_id>')
def get_client(client_id: int) -> Response:
    """
    Gets a client by id.
    :return: Response object
    """
    return make_response(jsonify(client_controller.find_by_id(client_id)), HTTPStatus.OK)

@client_bp.put('/<int:client_id>')
def update_client(client_id: int) -> Response:
    """
    Updates a client by id.
    :return: Response object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.update(client_id, client)
    return make_response("Client updated", HTTPStatus.OK)

@client_bp.patch('/<int:client_id>')
def patch_client(client_id: int) -> Response:
    """
    Patches a client by id.
    :return: Response object
    """
    content = request.get_json()
    client_controller.patch(client_id, content)
    return make_response("Client updated", HTTPStatus.OK)

@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    """
    Deletes a client by id.
    :return: Response object
    """
    client_controller.delete(client_id)
    return make_response("Client deleted", HTTPStatus.OK)

@client_bp.get('/insert-client/<string:first_name>/<string:last_name>/<string:phone>/'
               '<string:email>/<int:age>/<string:driver_license>')
def insert_client(first_name, last_name, phone, email, age, driver_license):
    client_controller.insert_client(first_name, last_name, phone, email, age, driver_license)
    return make_response("Client created", HTTPStatus.OK)
