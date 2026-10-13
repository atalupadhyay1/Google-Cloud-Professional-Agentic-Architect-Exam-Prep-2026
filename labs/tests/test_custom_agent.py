import unittest

from labs.agentic_workshop.custom_agent import CustomSupportAgent, MemoryBank, SessionStore
from labs.agentic_workshop.types import Caller


class CustomAgentTests(unittest.TestCase):
    def setUp(self):
        self.maya = Caller("maya", "northstar", frozenset({"employees"}))
        self.lee = Caller("lee", "northstar", frozenset({"employees"}))

    def test_session_isolated_by_user_and_tenant(self):
        sessions = SessionStore()
        sessions.append(self.maya, "same-browser-id", "user", "Maya's request")
        sessions.append(self.lee, "same-browser-id", "user", "Lee's request")
        self.assertEqual(len(sessions.history(self.maya, "same-browser-id")), 1)
        self.assertEqual(sessions.history(self.lee, "same-browser-id")[0].text, "Lee's request")
        another_tenant = Caller("maya", "otherco", frozenset({"employees"}))
        self.assertEqual(sessions.history(another_tenant, "same-browser-id"), ())

    def test_custom_agent_records_request_and_response_in_session(self):
        agent = CustomSupportAgent()
        result = agent.respond("How do I set up MFA?", self.maya, "session-1")
        history = agent.sessions.history(self.maya, "session-1")
        self.assertEqual(result.status, "answered")
        self.assertEqual([turn.role for turn in history], ["user", "assistant"])

    def test_memory_allows_only_small_non_sensitive_preferences(self):
        memory = MemoryBank()
        self.assertTrue(memory.remember(self.maya, "response_style", "concise"))
        self.assertEqual(memory.profile(self.maya), {"response_style": "concise"})
        self.assertFalse(memory.remember(self.maya, "password", "not-a-real-secret"))
        self.assertFalse(memory.remember(self.maya, "response_style", "one-time code: 123456"))
        self.assertEqual(memory.profile(self.lee), {})

    def test_memory_can_be_deleted(self):
        memory = MemoryBank()
        memory.remember(self.maya, "preferred_language", "English")
        memory.forget(self.maya, "preferred_language")
        self.assertEqual(memory.profile(self.maya), {})
        memory.remember(self.maya, "response_style", "brief")
        memory.forget(self.maya)
        self.assertEqual(memory.profile(self.maya), {})

    def test_empty_session_id_is_rejected(self):
        sessions = SessionStore()
        with self.assertRaises(ValueError):
            sessions.append(self.maya, " ", "user", "hello")


if __name__ == "__main__":
    unittest.main()
