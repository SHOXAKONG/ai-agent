from base_agent import BaseAgent
from data.mock_data import INVENTORY_DATA


class InventoryAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    @property
    def system_prompt(self) -> str:
        return (
            "You are an Inventory Intelligence Agent. "
            "You analyze stock levels, SKU performance, reorder points, and turnover rates. "
            "Flag items below reorder point as urgent. "
            "Be precise with numbers, mention SKU codes when relevant, "
            "and recommend reorder actions when stock is critically low."
        )

    @property
    def domain_data(self) -> dict:
        return INVENTORY_DATA
