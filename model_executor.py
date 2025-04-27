from typing import Optional
import openai
from backend.config.settings import settings

openai.api_key = settings.OPENAI_API_KEY

async def query_openai(prompt: str, model: str = "gpt-4o", max_tokens: int = 1000) -> Optional[str]:
    try:
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"OpenAI Query Failed: {e}")
        return None
