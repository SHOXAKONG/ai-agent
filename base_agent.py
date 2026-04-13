import asyncio
from abc import ABC, abstractmethod
from typing import AsyncIterator
from google import genai
from google.genai import types


class BaseAgent(ABC):
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        pass

    @property
    @abstractmethod
    def domain_data(self) -> dict:
        pass

    async def stream(
        self, messages: list[dict], user_query: str
    ) -> AsyncIterator[str]:
        history = [
            types.Content(
                role="user" if m["role"] == "user" else "model",
                parts=[types.Part(text=m["content"])],
            )
            for m in messages
        ]

        full_query = (
            f"Relevant data for this query:\n{self.domain_data}\n\n"
            f"User question: {user_query}"
        )

        history.append(
            types.Content(
                role="user",
                parts=[types.Part(text=full_query)],
            )
        )

        max_retries = 2
        delay = 5

        for attempt in range(max_retries):
            try:
                async for chunk in await self.client.aio.models.generate_content_stream(
                    model="gemini-2.5-flash",
                    contents=history,
                    config=types.GenerateContentConfig(
                        system_instruction=self.system_prompt,
                    ),
                ):
                    if chunk.text:
                        yield chunk.text
                return
            except Exception as e:
                if "429" in str(e) and attempt < max_retries - 1:
                    yield f"\n\n_Rate limited, retrying in {delay}s…_\n\n"
                    await asyncio.sleep(delay)
                    delay *= 2
                else:
                    raise