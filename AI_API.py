import openai
import os
import dotenv
def get_help(data: str, device: str,model="text-curie-001",temp=0.3) -> str:
    # Nastavení OpenAI API klíče
    dotenv.load_dotenv("locales.env")
    openai.api_key = os.getenv('openAIkey')

    # Příprava dotazu
    prompt = f"""Smart Home Energy Report

    Usage Patterns:
    {data}

    Question: How can I optimize the usage of my smart {device} system based on these usage patterns?"""

    # Volání OpenAI API
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=temp
    )

    # Získání odpovědi
    answer = response.choices[0].text.strip()

    # Výstup odpovědi
    return answer
