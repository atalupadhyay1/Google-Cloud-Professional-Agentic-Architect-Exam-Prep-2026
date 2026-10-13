import unittest

from labs.agentic_workshop.coding_agent import (
    MockMCPToolServer,
    PolicyDenied,
    SandboxPolicy,
    patch_comparison,
)


class CodingAgentTests(unittest.TestCase):
    def test_before_after_patch_has_behavior_and_security_evidence(self):
        results = patch_comparison()
        self.assertFalse(results["before"]["passed"])
        self.assertTrue(results["before"]["benign_input_preserved"])
        self.assertFalse(results["before"]["injection_remains_data"])
        self.assertTrue(results["after"]["passed"])

    def test_allowlisted_tool_works(self):
        server = MockMCPToolServer()
        result = server.call("run_unit_tests", test_suite="security")
        self.assertEqual(result["result"], "simulated tests passed")

    def test_unapproved_shell_tool_is_denied(self):
        server = MockMCPToolServer()
        with self.assertRaises(PolicyDenied):
            server.call("shell", command="printenv")

    def test_path_traversal_and_out_of_scope_paths_are_denied(self):
        policy = SandboxPolicy()
        with self.assertRaises(PolicyDenied):
            policy.authorize("read_scoped_file", path="src/../../secrets.env")
        with self.assertRaises(PolicyDenied):
            policy.authorize("read_scoped_file", path="docs/internal.md")

    def test_network_and_secrets_are_denied_by_default(self):
        policy = SandboxPolicy()
        with self.assertRaises(PolicyDenied):
            policy.authorize("run_unit_tests", network=True)
        with self.assertRaises(PolicyDenied):
            policy.authorize("run_unit_tests", needs_secret=True)

    def test_patch_tool_is_scoped_to_repository_roots(self):
        server = MockMCPToolServer()
        result = server.call("propose_patch", path="src/handler.py", summary="parameterize query")
        self.assertIn("human review required", result["result"])
        with self.assertRaises(PolicyDenied):
            server.call("propose_patch", path="production/config.yaml", summary="change config")


if __name__ == "__main__":
    unittest.main()
