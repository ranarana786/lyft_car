from unittest import TestCase
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(TestCase):
    # class that will test the cauplet engine
    def test_need_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
    def test_need_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

