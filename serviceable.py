from abc import ABC,abstractmethod

class Serviceable(ABC):
    # interface class that will check the is_servive_need functionaility in car
    def need_service(self):
        pass