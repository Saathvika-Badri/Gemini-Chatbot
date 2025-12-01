import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("Gemini_api_key"))

# Enable Google Search Grounding
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    tools=[{
        "google_search": {}
    }]
)

def get_gemini_response(prompt):
    response = model.generate_content(
        prompt,
        # Tell Gemini you WANT grounding
        grounding_config={
            "sources": ["google_search"]
        }
    )
    return response.text
