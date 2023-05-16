import openai
import os
import dotenv

# Nastavení OpenAI API klíče
dotenv.load_dotenv("locales.env")
openai.api_key = os.getenv('openAIkey')

# Příprava dotazu
prompt = """Smart Home Energy Report

Usage Patterns:

- 2023-05-15 08:00: ON OFF ON OFF ON
- 2023-05-15 12:30: ON OFF ON ON OFF
- 2023-05-15 18:45: ON ON OFF OFF ON

Question: How can I optimize the usage of my smart lighting system based on these usage patterns?"""

# Volání OpenAI API
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7
)

# Získání odpovědi
answer = response.choices[0].text.strip()

# Výstup odpovědi
print(answer)