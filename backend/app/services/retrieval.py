from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    source_id: str
    source_type: str
    excerpt: str
    score: float


class RetrievalService:
    """Placeholder retriever. Replace with FAISS/pgvector implementation."""

    def search(self, query: str, top_k: int) -> list[RetrievedChunk]:
        # TODO: implement embedding + vector search.
        return [
            RetrievedChunk(
                source_id="policy-001",
                source_type="policy",
                excerpt="Exposure breaches above threshold must be escalated within 24 hours.",
                score=0.92,
            )
        ][:top_k]
