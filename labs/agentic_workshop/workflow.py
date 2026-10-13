"""A small, explicit support state machine used in Labs 1, 3, and 6."""

from __future__ import annotations

import re

from .knowledge import KnowledgeBase
from .types import Caller, WorkflowResult

_INJECTION = re.compile(
    r"\b(ignore|disregard|bypass)\b.{0,60}\b(instructions|rules|policy|system)\b"
    r"|\breveal\b.{0,40}\b(secret|credential|token)\b",
    re.IGNORECASE,
)
_SECRET_ASSIGNMENT = re.compile(
    r"\b(password|token|one[- ]time code|recovery code|api key)\b\s*[:=]\s*\S+"
    r"|\bmy password is\b",
    re.IGNORECASE,
)
_HIGH_IMPACT = re.compile(
    r"\b(grant|give|add)\b.{0,50}\b(admin|administrator|privileged access|permissions?)\b"
    r"|\b(delete|remove)\b.{0,30}\b(account|data|record)\b"
    r"|\b(approve|pay|transfer)\b.{0,40}\b(invoice|funds|payment)\b",
    re.IGNORECASE,
)


class SupportWorkflow:
    """Deterministic reference flow; it does not call a language model."""

    def __init__(self, knowledge_base: KnowledgeBase | None = None):
        self.knowledge_base = knowledge_base or KnowledgeBase.default()

    def run(self, question: str, caller: Caller) -> WorkflowResult:
        trace = ["start", "authenticate"]
        clean_question = question.strip()
        if not caller.authenticated:
            trace.append("denied")
            return WorkflowResult(
                status="denied",
                answer="Please sign in through the approved company portal before I look up support information.",
                state_trace=trace,
            )
        if not clean_question:
            trace.extend(["classify", "clarify"])
            return WorkflowResult(
                status="clarify",
                answer="I’m ready to help. What are you trying to do, and what message are you seeing? Please leave out passwords and verification codes.",
                state_trace=trace,
            )

        trace.append("classify")
        trace.append("guardrail")
        if _INJECTION.search(clean_question):
            trace.append("blocked")
            return WorkflowResult(
                status="blocked",
                answer="I can’t follow instructions to bypass my support rules or reveal protected information. If you have a normal support question, tell me what task you’re working on and I’ll look for an approved guide.",
                state_trace=trace,
            )
        if _SECRET_ASSIGNMENT.search(clean_question):
            trace.append("blocked")
            return WorkflowResult(
                status="blocked",
                answer="For your safety, please remove that password or code from the message and rotate it if it was real. I don’t need secrets to help; use the approved identity-support channel.",
                state_trace=trace,
            )
        if _HIGH_IMPACT.search(clean_question):
            trace.extend(["policy_check", "handoff"])
            return WorkflowResult(
                status="escalate",
                answer="I can’t grant privileged access or make that change from chat. I can help you find the approved request path; an authorized owner must review it.",
                state_trace=trace,
                handoff_to="authorized_support_owner",
            )

        trace.append("retrieve_authorized_sources")
        hits = self.knowledge_base.search(clean_question, caller, top_k=2)
        if not hits:
            trace.append("clarify")
            return WorkflowResult(
                status="clarify",
                answer="I couldn’t find an approved, current guide that answers that yet. Could you share the product or error message (without personal data)? If it’s urgent, I can route this to the support team.",
                state_trace=trace,
                handoff_to="support_queue",
            )

        best = hits[0]
        trace.extend(["compose_with_evidence", "done"])
        answer = (
            f"I can help. The approved guide ‘{best.title}’ says: {best.excerpt} "
            f"Source: {best.document_id}, version {best.version}. "
            "Please don’t paste a password, one-time code, recovery code, or access token here."
        )
        return WorkflowResult(
            status="answered",
            answer=answer,
            state_trace=trace,
            source_ids=[best.document_id],
        )
