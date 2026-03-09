# Architecture (Starter)

## Core flow

1. Ingestion: policy docs, annual reports, and structured tables
2. Chunk + embed: create vector index for unstructured text
3. Retrieval: fetch relevant chunks for a question
4. SQL tool: execute guarded query for structured facts
5. Synthesis: generate grounded answer with citations

## Components

- `app/services/ingestion.py`: ingestion pipeline
- `app/services/retrieval.py`: vector search
- `app/services/sql_tool.py`: NL2SQL + execution guardrails
- `app/services/synthesizer.py`: grounded response generation
- `app/services/orchestrator.py`: retriever -> SQL -> synthesis chain

## Next upgrades

- Add LangGraph state machine
- Add evaluator endpoints and offline benchmark job
- Add per-request observability and prompt versioning
