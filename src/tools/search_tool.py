import os

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool


load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def search_tool(query: str) -> list[dict]:
    """Search the web for jobs and internships."""

    query = query[:1500]

    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return response.get("results", [])