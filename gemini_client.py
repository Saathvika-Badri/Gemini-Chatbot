from tool_search import response  # Import the response from your existing tool_search

def get_gemini_response(user_input):
    """
    Currently, your tool_search.py generates a static response.
    We'll modify it to accept dynamic input.
    """
    from google import genai
    from google.genai import types
    import os

    client = genai.Client()

    search_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    config = types.GenerateContentConfig(
        tools=[search_tool]
    )

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config=config
    )

    return resp.text
