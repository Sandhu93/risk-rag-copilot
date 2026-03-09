# RiskRAG Copilot

In development of a risk/compliance Retrieval-Augmented Generation (RAG) copilot.

## What it includes

- FastAPI backend scaffold
- Modular service layer for:
  - document ingestion
  - retrieval
  - SQL tool execution
  - response synthesis
- Grounded answer response schema with citations
- Token and latency logging hooks
- Docker + docker-compose setup
- Sample data placeholders
- Docs placeholders for architecture and tradeoffs

## Quick start

1. Copy env file:

```bash
cp .env.example .env
```

2. Run with Docker:

```bash
docker compose up --build
```

3. Open API docs:

- http://localhost:8000/docs

## Local run (without Docker)

```bash
cd backend
python -m venv .venv
# Windows
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## build order

1. Implement ingestion pipeline (`app/services/ingestion.py`)
2. Add embeddings + vector DB (`app/services/retrieval.py`)
3. Connect Postgres and SQL safety layer (`app/services/sql_tool.py`)
4. Improve orchestration and guardrails (`app/services/orchestrator.py`)
5. Add eval pipeline + benchmark notebook
6. Add auth, rate limits, and audit logs

## Repo structure

See `docs/architecture.md` for the high-level design.
