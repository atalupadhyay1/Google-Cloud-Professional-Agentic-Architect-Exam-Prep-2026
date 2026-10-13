import unittest

from labs.agentic_workshop.evaluation import EvaluationRunner, default_evalset
from labs.agentic_workshop.operations import (
    RuntimeRequirements,
    TraceRecord,
    choose_runtime,
    release_gate,
    summarize_traces,
)


class EvaluationTests(unittest.TestCase):
    def test_synthetic_golden_set_passes(self):
        summary = EvaluationRunner().run()
        self.assertEqual(summary.total, len(default_evalset()))
        self.assertTrue(summary.all_passed)
        self.assertEqual(summary.pass_rate, 1.0)


class OperationsTests(unittest.TestCase):
    def test_runtime_choice_follows_stated_constraints(self):
        self.assertEqual(choose_runtime(RuntimeRequirements(managed_agent_lifecycle_fit=True)).name, "Agent Runtime")
        self.assertEqual(choose_runtime(RuntimeRequirements(request_driven_http=True)).name, "Cloud Run")
        self.assertEqual(
            choose_runtime(RuntimeRequirements(needs_kubernetes_control=True, team_can_operate_kubernetes=True)).name,
            "GKE",
        )
        self.assertEqual(
            choose_runtime(RuntimeRequirements(needs_kubernetes_control=True, team_can_operate_kubernetes=False)).name,
            "revisit-requirements",
        )

    def test_trace_summary_uses_privacy_safe_metadata(self):
        summary = summarize_traces(
            [
                TraceRecord("r1", "v1", "answered", 100, ("search",)),
                TraceRecord("r2", "v1", "timeout", 500, ("search",), error_kind="timeout"),
                TraceRecord("r3", "v1", "completed", 200),
                TraceRecord("r4", "v1", "clarify", 150),
            ]
        )
        self.assertEqual(summary.requests, 4)
        self.assertEqual(summary.failures, 1)
        self.assertAlmostEqual(summary.error_rate, 1 / 4)
        self.assertEqual(summary.p95_duration_ms, 500)
        self.assertEqual(summary.tool_calls, 2)

    def test_release_gate_approves_only_when_every_gate_is_met(self):
        approved = release_gate(
            evaluation_pass_rate=1.0,
            security_cases_pass=True,
            denied_path_tested=True,
            canary_error_rate=0.01,
            rollback_defined=True,
        )
        self.assertTrue(approved.approved)
        blocked = release_gate(
            evaluation_pass_rate=0.9,
            security_cases_pass=False,
            denied_path_tested=False,
            canary_error_rate=0.1,
            rollback_defined=False,
        )
        self.assertFalse(blocked.approved)
        self.assertGreaterEqual(len(blocked.reasons), 4)


if __name__ == "__main__":
    unittest.main()
