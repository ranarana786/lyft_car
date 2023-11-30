from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tier.octoprimes_tier import OctoprimesTier
from tier.carrigan_tier import CarriganTier


class CarFactory:
    # Class that will make all model of class hold method for each car model creation
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_millage, last_millage,tier_wear_array,check_number):
        engine = CapuletEngine(current_millage, last_millage)
        battery = SpindlerBattery(current_date, last_service_date)
        tier = CarriganTier(tier_wear_array,check_number)
        car = Car(engine == engine, battery=battery,tier = tier)
        return car

    @staticmethod
    def create_gallisade(self,current_date, last_service_date, current_millage, last_millage,tier_wear_array,check_number):
        engine = WilloughbyEngine(current_millage, last_millage)
        battery = SpindlerBattery(current_date, last_service_date)
        tier = OctoprimesTier(tier_wear_array, check_number)
        car = Car(engine == engine, battery=battery, tier=tier)
        return car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_millage, last_millage,tier_wear_array,check_number):
        engine = CapuletEngine(current_millage, last_millage)
        battery = NubbinBattery(current_date, last_service_date)
        tier = CarriganTier(tier_wear_array, check_number)
        car = Car(engine == engine, battery=battery, tier=tier)
        return car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_millage, last_millage,tier_wear_array,check_number):
        engine = WilloughbyEngine(current_millage, last_millage)
        battery = NubbinBattery(current_date, last_service_date)
        tier = OctoprimesTier(tier_wear_array, check_number)
        car = Car(engine == engine, battery=battery, tier=tier)

        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on,tier_wear_array,check_number):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tier = CarriganTier(tier_wear_array,check_number)
        car = Car(engine == engine, battery=battery,tier=tier)
        return car

