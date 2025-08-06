import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("TAVILY_API_KEY")

# Handle missing key
if not api_key:
    raise ValueError("Tavily API Key is missing. Please add it to the .env file.")

client = TavilyClient(api_key)

def search_news(query):
    response = client.search(
        query=query,
        search_depth="advanced",  # deeper search
        include_answer=True,
        include_raw_content=True,
        max_results=5
    )
    return response["results"]
