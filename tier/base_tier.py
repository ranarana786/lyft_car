from abc import ABC, abstractmethod


class Tier(ABC):
    # Tier interface class that will be implemented by all child tier classes
    @abstractmethod
    def should_tier_need_service(self):
        pass
