from unittest import TestCase
from tier.octoprimes_tier import OctoprimesTier


class TestOctoprimesTier(TestCase):
    def test_cctoprimes_need_service_true(self):
        self.octoprimes_tier = OctoprimesTier([0.9, 0.1, 0.2, 0.8], 3)
        result = self.octoprimes_tier.should_tier_need_service()
        self.assertTrue(result)

    def test_octoprimes_need_service_false(self):
        self.octoprimes_tier = OctoprimesTier([0.9, 0.1, 0.2, 0.8], 3)
        result = self.octoprimes_tier.should_tier_need_service()
        self.assertFalse(result)
