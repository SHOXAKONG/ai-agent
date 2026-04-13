from typing import AsyncIterator
from google import genai

from agents.sales_agent import SalesAgent
from agents.inventory_agent import InventoryAgent
from agents.finance_agent import FinanceAgent
from agents.hr_agent import HRAgent
from agents.general_agent import GeneralAgent

DOMAIN_MAP = {
    "sales": SalesAgent,
    "inventory": InventoryAgent,
    "finance": FinanceAgent,
    "hr": HRAgent,
    "general": GeneralAgent,
}

KEYWORDS = {
    "sales": ["sale", "revenue", "deal", "pipeline", "win rate", "region", "quota", "closing"],
    "inventory": ["stock", "sku", "inventory", "reorder", "turnover", "product", "warehouse"],
    "finance": ["profit", "expense", "budget", "margin", "p&l", "cost", "finance", "spending"],
    "hr": ["employee", "headcount", "hire", "turnover", "tenure", "staff", "department", "people"],
}


def classify_intent_local(query: str) -> str:
    q = query.lower()
    scores = {domain: 0 for domain in KEYWORDS}
    for domain, words in KEYWORDS.items():
        for word in words:
            if word in q:
                scores[domain] += 1
    best = max(scores, key=lambda d: scores[d])
    return best if scores[best] > 0 else "general"


class Orchestrator:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def stream_response(
        self,
        query: str,
        history: list[dict],
    ) -> AsyncIterator[str]:
        intent = classify_intent_local(query)
        agent_class = DOMAIN_MAP[intent]
        agent = agent_class(self.api_key)

        async for token in agent.stream(history, query):
            yield token