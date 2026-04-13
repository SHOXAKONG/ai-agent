from base_agent import BaseAgent
from data.mock_data import SALES_DATA


class SalesAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    @property
    def system_prompt(self) -> str:
        return (
            "You are a Sales Intelligence Agent for a B2B company. "
            "You analyze sales data and answer questions about revenue, deals, "
            "win rates, pipeline stages, and regional performance. "
            "Be concise, use numbers precisely, and highlight trends or anomalies. "
            "Format monetary values with $ and commas. "
            "When relevant, suggest actionable next steps."
        )

    @property
    def domain_data(self) -> dict:
        return SALES_DATA