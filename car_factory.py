from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    # Class that will make all model of class hold method for each car model creation
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_millage, last_millage):
        engine = CapuletEngine(current_millage, last_millage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine == engine, battery=battery)
        return car

    @staticmethod
    def create_gallisade(self,current_date, last_service_date, current_millage, last_millage):
        engine = WilloughbyEngine(current_millage, last_millage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine == engine, battery=battery)
        return car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_millage, last_millage):
        engine = CapuletEngine(current_millage, last_millage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine == engine, battery=battery)
        return car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_millage, last_millage):
        engine = WilloughbyEngine(current_millage, last_millage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine == engine, battery=battery)
        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine == engine, battery=battery)
        return car

