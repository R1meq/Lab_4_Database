from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import country_controller
from t08_flask_mysql.app.my_project.auth.domain import Country

country_bp = Blueprint('country', __name__, url_prefix='/country')

@country_bp.get('')
def get_all_countries() -> Response:
    """
    Gets all objects from the country table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)


@country_bp.post('')
def create_country() -> Response:
    """
    Creates a country using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.CREATED)


@country_bp.get('/<int:country_id>')
def get_country(country_id: int) -> Response:
    """
    Gets a country by id.
    :return: Response object
    """
    return make_response(jsonify(country_controller.find_by_id(country_id)), HTTPStatus.OK)


@country_bp.put('/<int:country_id>')
def update_country(country_id: int) -> Response:
    """
    Updates a country by id.
    :return: Response object
    """
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.update(country_id, country)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.patch('/<int:country_id>')
def patch_country(country_id: int) -> Response:
    """
    Patches a country by id.
    :return: Response object
    """
    content = request.get_json()
    country_controller.patch(country_id, content)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.delete('/<int:country_id>')
def delete_country(country_id: int) -> Response:
    """
    Deletes a country by id.
    :return: Response object
    """
    country_controller.delete(country_id)
    return make_response("Country deleted", HTTPStatus.OK)

@country_bp.get('/insert_10_values')
def insert_10_values():
    country_controller.insert_10_values()
    return make_response("Values inserted",HTTPStatus.OK)