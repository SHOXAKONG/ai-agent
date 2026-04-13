from base_agent import BaseAgent
from data.mock_data import HR_DATA


class HRAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    @property
    def system_prompt(self) -> str:
        return (
            "You are an HR Intelligence Agent. "
            "You analyze headcount, hiring trends, turnover rates, tenure distribution, "
            "and workforce composition across departments. "
            "Be sensitive and professional. Express rates as percentages. "
            "Flag concerning turnover trends and highlight departments with open positions."
        )

    @property
    def domain_data(self) -> dict:
        return HR_DATA
