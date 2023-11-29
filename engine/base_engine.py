from abc import ABC, abstractmethod


class Engine(ABC):
    # Engine interface class that should be implemented by all subclass made from engine
    @abstractmethod
    def engine_should_be_serviced(self):
        # Abstract method check engine service
        pass
