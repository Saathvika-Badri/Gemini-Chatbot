from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()

# Define search tool
search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[search_tool]
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="recent ODI match between India and South africa",
    config=config
)

print(response.text)
