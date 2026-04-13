# Multi-Agent BI — Backend

FastAPI backend with multi-agent orchestration powered by Claude.

## Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Run

```bash
uvicorn main:app --reload --port 8000
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/chat` | SSE streaming chat — body: `{ query, history }` |
| GET | `/api/metrics/dashboard` | Top-level KPIs |
| GET | `/api/metrics/sales` | Sales data |
| GET | `/api/metrics/inventory` | Inventory data |
| GET | `/api/metrics/finance` | Finance data |
| GET | `/api/metrics/hr` | HR data |
| GET | `/api/health` | Health check |

## Chat SSE format

Each SSE event is one of:
- `data: {"token": "..."}` — streamed text chunk
- `data: [DONE]` — stream complete
- `data: {"error": "..."}` — error occurred

## Project structure

```
backend/
├── main.py              # FastAPI app, CORS, all routes
├── orchestrator.py      # intent classifier + agent router
├── agents/
│   ├── base_agent.py    # abstract base with stream()
│   ├── sales_agent.py
│   ├── inventory_agent.py
│   ├── finance_agent.py
│   ├── hr_agent.py
│   └── general_agent.py
├── data/
│   └── mock_data.py     # all mock datasets — swap for DB here
├── requirements.txt
└── .env.example
```

## Swapping mock data for a real DB

All data lives in `data/mock_data.py`. Each agent imports its own slice.
To connect a real database, replace the constants in `mock_data.py` with
async query functions and update the agent `domain_data` properties accordingly.
