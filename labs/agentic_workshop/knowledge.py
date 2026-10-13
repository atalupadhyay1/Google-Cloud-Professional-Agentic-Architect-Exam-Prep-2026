"""Permission-filtered toy retrieval for the local labs.

The ranker is lexical and intentionally tiny. It is not an embedding model,
vector database, production RAG system, or substitute for Google Cloud ACLs.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

from .types import Caller, SearchHit

_TOKEN_RE = re.compile(r"[a-z0-9]+", re.IGNORECASE)
_STOP_WORDS = {
    "a", "about", "an", "and", "are", "can", "do", "for", "how", "i",
    "in", "is", "it", "me", "my", "of", "on", "please", "the", "to",
    "what", "where", "with", "you",
}


@dataclass(frozen=True)
class Document:
    document_id: str
    title: str
    text: str
    version: str
    tenant: str
    allowed_groups: frozenset[str]
    valid_until: date | None

    @classmethod
    def from_dict(cls, raw: dict[str, object]) -> "Document":
        valid_until_raw = raw.get("valid_until")
        valid_until = date.fromisoformat(str(valid_until_raw)) if valid_until_raw else None
        return cls(
            document_id=str(raw["id"]),
            title=str(raw["title"]),
            text=str(raw["text"]),
            version=str(raw["version"]),
            tenant=str(raw["tenant"]),
            allowed_groups=frozenset(str(group) for group in raw.get("allowed_groups", [])),
            valid_until=valid_until,
        )


class KnowledgeBase:
    def __init__(self, documents: Iterable[Document]):
        self._documents = tuple(documents)

    @classmethod
    def from_json(cls, path: str | Path) -> "KnowledgeBase":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(Document.from_dict(item) for item in raw)

    @classmethod
    def default(cls) -> "KnowledgeBase":
        data_path = Path(__file__).parent / "data" / "knowledge.json"
        return cls.from_json(data_path)

    @staticmethod
    def _tokens(text: str) -> set[str]:
        return {
            token.lower()
            for token in _TOKEN_RE.findall(text)
            if token.lower() not in _STOP_WORDS and len(token) > 1
        }

    @staticmethod
    def _authorized(document: Document, caller: Caller, today: date) -> bool:
        if not caller.authenticated or document.tenant != caller.tenant:
            return False
        if document.valid_until is not None and document.valid_until < today:
            return False
        if document.allowed_groups and not document.allowed_groups.intersection(caller.groups):
            return False
        return True

    def search(
        self,
        query: str,
        caller: Caller,
        *,
        top_k: int = 3,
        today: date | None = None,
    ) -> list[SearchHit]:
        """Return lexical matches only after tenant, group, and freshness checks."""
        if top_k < 1:
            raise ValueError("top_k must be positive")
        query_tokens = self._tokens(query)
        if not query_tokens:
            return []
        effective_date = today or date.today()
        ranked: list[tuple[float, Document]] = []
        for document in self._documents:
            if not self._authorized(document, caller, effective_date):
                continue
            document_tokens = self._tokens(document.title + " " + document.text)
            overlap = query_tokens.intersection(document_tokens)
            if not overlap:
                continue
            # A small normalized lexical score; it is for teaching, not production ranking.
            score = len(overlap) / math.sqrt(len(query_tokens) * len(document_tokens))
            ranked.append((score, document))
        ranked.sort(key=lambda pair: (-pair[0], pair[1].document_id))
        return [
            SearchHit(
                document_id=document.document_id,
                title=document.title,
                excerpt=document.text,
                version=document.version,
                score=score,
            )
            for score, document in ranked[:top_k]
        ]

    def ids(self) -> tuple[str, ...]:
        """Expose document identifiers for tests; never returns document contents."""
        return tuple(document.document_id for document in self._documents)
