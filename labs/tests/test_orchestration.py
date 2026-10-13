import unittest

from labs.agentic_workshop.orchestration import (
    AgentCard,
    AgentDirectory,
    HandoffEnvelope,
    HandoffValidationError,
    run_graph,
    run_parallel,
    run_sequential,
)


class HandoffTests(unittest.TestCase):
    def test_valid_handoff_and_directory_discovery(self):
        envelope = HandoffEnvelope(
            "1", "task-1", "context-1", "triage", "research", "Find an approved article.",
            evidence_ids=("it.mfa.01",), constraints=("read-only",),
        )
        envelope.validate()
        directory = AgentDirectory()
        directory.register(AgentCard("research", frozenset({"support-search"}), "v1", "IT"))
        self.assertEqual(directory.discover("support-search")[0].agent_id, "research")
        self.assertEqual(directory.discover("payments"), ())

    def test_handoff_rejects_secret_and_unknown_schema(self):
        with self.assertRaises(HandoffValidationError):
            HandoffEnvelope("1", "t", "c", "a", "b", "token=secret").validate()
        with self.assertRaises(HandoffValidationError):
            HandoffEnvelope("99", "t", "c", "a", "b", "work").validate()


class WorkflowOrchestrationTests(unittest.TestCase):
    def test_sequential_dependencies_add_non_overlapping_state(self):
        result = run_sequential(
            [
                ("classify", lambda state: {"intent": "support"}),
                ("retrieve", lambda state: {"source": "it.mfa.01" if state["intent"] == "support" else "none"}),
                ("compose", lambda state: {"ready": bool(state["source"])}),
            ],
            {"question": "MFA"},
        )
        self.assertEqual(result.status, "complete")
        self.assertTrue(result.state["ready"])
        self.assertEqual(result.trace, ("classify", "retrieve", "compose"))

    def test_sequential_timeout_stops_downstream_work(self):
        result = run_sequential(
            [("first", lambda state: {"one": 1}), ("second", lambda state: {"two": 2})],
            {},
            fail_node="second",
        )
        self.assertEqual(result.status, "failed")
        self.assertIn("one", result.state)
        self.assertNotIn("two", result.state)
        self.assertEqual(len(result.errors), 1)

    def test_sequential_state_overwrite_is_rejected(self):
        result = run_sequential(
            [("unsafe", lambda state: {"request": "overwritten"})],
            {"request": "original"},
        )
        self.assertEqual(result.status, "failed")
        self.assertEqual(result.state["request"], "original")

    def test_parallel_branches_merge_and_partial_failure_is_explicit(self):
        branches = {
            "knowledge": lambda state: {"evidence": "it.mfa.01"},
            "policy": lambda state: {"policy": "allow_read"},
        }
        complete = run_parallel(branches, {"request": "MFA"})
        self.assertEqual(complete.status, "complete")
        self.assertIn("policy", complete.state)
        partial = run_parallel(
            branches,
            {"request": "MFA"},
            fail_branches=frozenset({"policy"}),
            require_all=False,
        )
        self.assertEqual(partial.status, "partial")
        self.assertIn("evidence", partial.state)
        self.assertEqual(len(partial.errors), 1)
        strict = run_parallel(
            branches,
            {"request": "MFA"},
            fail_branches=frozenset({"policy"}),
            require_all=True,
        )
        self.assertEqual(strict.status, "failed")
        self.assertNotIn("evidence", strict.state)

    def test_parallel_conflicting_output_key_fails_closed(self):
        result = run_parallel(
            {
                "branch-a": lambda state: {"decision": "allow"},
                "branch-b": lambda state: {"decision": "deny"},
            },
            {},
        )
        self.assertEqual(result.status, "failed")
        self.assertTrue(any("conflicting" in error for error in result.errors))

    def test_graph_routes_and_terminates(self):
        result = run_graph(
            "classify",
            {
                "classify": lambda state: {"intent": "support"},
                "answer": lambda state: {"status": "grounded"},
            },
            lambda name, output: "answer" if name == "classify" else None,
            {"request_id": "r1"},
        )
        self.assertEqual(result.status, "complete")
        self.assertEqual(result.trace, ("classify", "answer"))
        self.assertEqual(result.state["status"], "grounded")

    def test_graph_unknown_route_and_step_limit_are_reported(self):
        unknown = run_graph(
            "start", {"start": lambda state: {"ok": True}},
            lambda name, output: "missing", {},
        )
        self.assertEqual(unknown.status, "failed")
        self.assertIn("unknown route", unknown.errors[0])
        looping = run_graph(
            "loop", {"loop": lambda state: {}}, lambda name, output: "loop", {}, max_steps=3
        )
        self.assertEqual(looping.status, "failed")
        self.assertEqual(looping.errors, ("step_limit_exceeded",))


if __name__ == "__main__":
    unittest.main()
