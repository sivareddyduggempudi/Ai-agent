import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
serpapi_key = os.getenv("SERPAPI_API_KEY")


genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("models/gemini-2.0-pro-exp-02-05")

def google_search(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google",
        "num": 3
    }
    res = requests.get(url, params=params)
    results = res.json()
    links = []
    for r in results.get("organic_results", []):
        links.append(r["link"])
    return links

def scrape_page(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join(p.get_text() for p in paragraphs)
        return text[:3000]  
    except:
        return ""

def ask_agent(query):
    links = google_search(query)
    source_contexts = []

    for link in links:
        page = scrape_page(link)
        if page:
            source_contexts.append((link, page[:3000]))

    if not source_contexts:
        return "❌ Sorry, no relevant content was found."

    # Build a citation-aware prompt
    prompt = f"""You are a helpful AI agent. Use only the information provided in the sources below to answer the question: "{query}".

Cite your sources in markdown format like this: [source](https://example.com). For every fact you state, include its citation after the sentence.

### Sources:
"""

    for i, (url, text) in enumerate(source_contexts):
        prompt += f"Source {i+1} - {url}:\n{text}\n\n"

    prompt += "\n### Answer:\n"

    response = model.generate_content(prompt)
    return response.text

