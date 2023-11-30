from tier.carrigan_tier import CarriganTier
from unittest import TestCase


class TestCarriganTier(TestCase):
    def test_carrigan_need_service_true(self):
        self.carrigan_tier = CarriganTier([0.9, 0.1, 0.2, 0.8], 0.8)
        result = self.carrigan_tier.should_tier_need_service()
        self.assertTrue(result)

    def test_carrigan_need_service_false(self):
        self.carrigan_tier = CarriganTier([0.9, 0.1, 0.2, 0.8], 0.3)
        result = self.carrigan_tier.should_tier_need_service()
        self.assertFalse(result)
