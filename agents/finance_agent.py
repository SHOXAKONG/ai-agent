from base_agent import BaseAgent
from data.mock_data import FINANCE_DATA


class FinanceAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    @property
    def system_prompt(self) -> str:
        return (
            "You are a Finance Intelligence Agent. "
            "You analyze P&L statements, expense breakdowns, budget vs actuals, "
            "and profitability trends. "
            "Use precise financial language, express margins as percentages, "
            "and flag departments that are over budget. "
            "Provide context for variances when possible."
        )

    @property
    def domain_data(self) -> dict:
        return FINANCE_DATA
