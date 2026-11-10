import copy
import json
from pathlib import Path
import unittest

from agent import analyze


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path(__file__).with_name("example.json").read_text())

    def test_example_distinguishes_known_and_unknown_exposure(self):
        self.assertEqual(
            [row["priority"] for row in analyze(self.data)["findings"]],
            ["urgent_review", "investigate_exposure", "scheduled_review"],
        )

    def test_active_exploitation_escalates_affected_internal_asset(self):
        self.data["exploitation"] = "active"
        self.assertEqual(analyze(self.data)["findings"][2]["priority"], "urgent_review")

    def test_missing_facts_never_become_scheduled_review(self):
        from itertools import product

        for exploitation, exposure, criticality in product(
            ["active", "not_reported", "unknown"],
            ["internet", "internal", "unknown"],
            ["high", "standard", "unknown"],
        ):
            self.data["exploitation"] = exploitation
            asset = copy.deepcopy(self.data["assets"][0])
            asset.update(exposure=exposure, criticality=criticality)
            self.data["assets"] = [asset]
            if "unknown" in (exploitation, exposure, criticality):
                with self.subTest(
                    exploitation=exploitation,
                    exposure=exposure,
                    criticality=criticality,
                ):
                    self.assertNotEqual(
                        analyze(self.data)["findings"][0]["priority"],
                        "scheduled_review",
                    )

    def test_non_applicability_requires_evidence(self):
        self.data["assets"][0].update(affected="no", evidence_ids=[])
        with self.assertRaises(ValueError):
            analyze(self.data)

    def test_unknown_affected_state_is_never_deferred(self):
        self.data["exploitation"] = "active"
        self.assertEqual(
            analyze(self.data)["findings"][1]["priority"], "investigate_exposure"
        )

    def test_unsupported_policy_value_is_rejected(self):
        self.data["assets"][0]["criticality"] = "probably-low"
        with self.assertRaises(ValueError):
            analyze(self.data)


if __name__ == "__main__":
    unittest.main()
