"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from .orders.country_controller import CountryController
from .orders.region_controller import RegionController
from .orders.city_controller import CityController
from .orders.rental_agency_controller import RentalAgencyController
from .orders.location_controller import LocationController
from .orders.client_controller import ClientController
from .orders.rent_controller import RentController
from .orders.vehicle_controller import VehicleController
from .orders.rent_option_controller import RentOptionController
from .orders.option_controller import OptionController
from .orders.fine_controller import FineController


rent_option_controller = RentOptionController()
option_controller = OptionController()
fine_controller = FineController()
client_controller = ClientController()
rent_controller = RentController()
vehicle_controller = VehicleController()
country_controller = CountryController()
region_controller = RegionController()
city_controller = CityController()
rental_agency_controller = RentalAgencyController()
location_controller = LocationController()
