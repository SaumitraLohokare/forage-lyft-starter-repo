from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire
from datetime import datetime

class CarFactory():
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(wear)
        return Car(engine, battery, tire)

    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(wear)
        return Car(engine, battery, tire)

    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, wear) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTire(wear)
        return Car(engine, battery, tire)

    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(wear)
        return Car(engine, battery, tire)

    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTire(wear)
        return Car(engine, battery, tire)



