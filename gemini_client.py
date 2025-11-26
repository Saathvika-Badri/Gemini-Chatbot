import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("Gemini_api_key"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text
