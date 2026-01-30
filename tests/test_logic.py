import unittest
from core.decision_engine import aggregate_signals

class TestDecisionLogic(unittest.TestCase):
    def test_rule_8_critical_ai_ncii(self):
        # AI + NSFW + Shielded
        result = aggregate_signals(nsfw_score=0.9, identity_found=True, is_shielded=True, ai_score=0.8)
        self.assertEqual(result, "CRITICAL_AI_NCII_BLOCK")

    def test_rule_4_critical_ncii(self):
        # Real + NSFW + Shielded
        result = aggregate_signals(nsfw_score=0.9, identity_found=True, is_shielded=True, ai_score=0.1)
        self.assertEqual(result, "CRITICAL_NCII_BLOCK")

    def test_rule_6_synthetic_identity(self):
        # AI + SFW + Shielded
        result = aggregate_signals(nsfw_score=0.2, identity_found=True, is_shielded=True, ai_score=0.8)
        self.assertEqual(result, "SYNTHETIC_IDENTITY_BLOCK")

    def test_rule_5_7_approved_synthetic(self):
        # AI + Consensual
        result = aggregate_signals(nsfw_score=0.1, identity_found=True, is_shielded=False, ai_score=0.8)
        self.assertEqual(result, "APPROVED_SYNTHETIC_CONTENT")

    def test_rule_1_safe_release(self):
        # Real + SFW + Consensual
        result = aggregate_signals(nsfw_score=0.1, identity_found=False, is_shielded=False, ai_score=0.1)
        self.assertEqual(result, "SAFE_OR_RELEASE")

if __name__ == "__main__":
    unittest.main()