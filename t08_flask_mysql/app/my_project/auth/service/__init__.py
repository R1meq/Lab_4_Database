"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""


from .orders.country_service import CountryService
from .orders.city_service import CityService
from .orders.region_service import RegionService
from .orders.location_service import LocationService
from .orders.rental_agency_service import RentalAgencyService
from .orders.rent_service import RentService
from .orders.client_service import ClientService
from .orders.vehicle_service import VehicleService
from .orders.rent_option_service import RentOptionService
from .orders.option_service import OptionService
from .orders.fine_service import FineService

rent_option_service = RentOptionService()
option_service = OptionService()
fine_service = FineService()
rent_service = RentService()
client_service = ClientService()
vehicle_service = VehicleService()
country_service = CountryService()
city_service = CityService()
region_service = RegionService()
location_service = LocationService()
rental_agency_service = RentalAgencyService()
