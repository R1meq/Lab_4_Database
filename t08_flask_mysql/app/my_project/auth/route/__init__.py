"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.region_route import region_bp
    from .orders.country_route import country_bp
    from .orders.city_route import city_bp
    from .orders.rental_agency_route import rental_agency_bp
    from .orders.location_route import location_bp
    from .orders.client_route import client_bp
    from .orders.vehicle_route import vehicle_bp
    from .orders.rent_route import rent_bp
    from .orders.fine_route import fine_bp
    from .orders.rent_option_route import rent_option_bp
    from .orders.option_route import option_bp

    app.register_blueprint(fine_bp)
    app.register_blueprint(rent_option_bp)
    app.register_blueprint(option_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(vehicle_bp)
    app.register_blueprint(rent_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(rental_agency_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(country_bp)

