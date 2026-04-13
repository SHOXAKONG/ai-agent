from base_agent import BaseAgent
from data.mock_data import (
    SALES_DATA, INVENTORY_DATA, FINANCE_DATA, HR_DATA, DASHBOARD_KPIS
)


class GeneralAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    @property
    def system_prompt(self) -> str:
        return (
            "You are a General Business Intelligence Agent with access to all company data. "
            "You handle cross-domain questions and queries that span multiple departments. "
            "Synthesize insights from sales, inventory, finance, and HR data. "
            "Be concise, highlight the most important numbers, and connect insights across domains."
        )

    @property
    def domain_data(self) -> dict:
        return {
            "dashboard_kpis": DASHBOARD_KPIS,
            "sales_kpis": SALES_DATA["kpis"],
            "inventory_kpis": INVENTORY_DATA["kpis"],
            "finance_kpis": FINANCE_DATA["kpis"],
            "hr_kpis": HR_DATA["kpis"],
        }
