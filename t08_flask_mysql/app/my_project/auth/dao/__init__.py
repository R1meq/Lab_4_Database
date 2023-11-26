"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.city_dao import CityDAO
from .orders.region_dao import RegionDAO
from .orders.location_dao import LocationDAO
from .orders.rental_agency_dao import RentalAgencyDAO
from .orders.country_dao import CountryDAO
from .orders.vehicle_dao import VehicleDAO
from .orders.rent_dao import RentDAO
from .orders.client_dao import ClientDAO
from .orders.fine_dao import FineDAO
from .orders.option_dao import OptionDAO
from .orders.rent_option_dao import RentOptionDAO

fine_dao = FineDAO()
option_dao = OptionDAO()
rent_option_dao = RentOptionDAO()
vehicle_dao = VehicleDAO()
rent_dao = RentDAO()
client_dao = ClientDAO()
country_dao = CountryDAO()
city_dao = CityDAO()
region_dao = RegionDAO()
location_dao = LocationDAO()
rental_agency_dao = RentalAgencyDAO()
