# configs/search_module.py

import requests
import json
from configs.Api_search_configator import API_KEY, SEARCH_ENGINE_ID

def perform_search(query):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": API_KEY,
            "cx": SEARCH_ENGINE_ID,
            "q": query
        }

        response = requests.get(url, params=params)
        data = response.json()

        results = []
        for item in data.get("items", [])[:3]:
            snippet = item.get("snippet")
            if snippet:
                results.append(snippet)

        return " | ".join(results) if results else "No relevant results found."
    
    except Exception as e:
        return f"Error occurred while searching: {str(e)}"
