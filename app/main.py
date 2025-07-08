

from fastapi import FastAPI, Request, APIRouter
from typing import List, Dict, Any
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import FileResponse
import openai
import os
import traceback
import requests
import time

from app.scraper.amazon_us import scrape_amazon_us_bs4
from app.scraper.walmart_us import scrape_walmart_us
from app.scraper.bestbuy_us import scrape_bestbuy_us
from app.scraper.target_us import scrape_target_us
from app.scraper.flipkart_in import scrape_flipkart_in

# 1. Initialize FastAPI FIRST
app = FastAPI()

# 2. Mount static files directory for UI (index.html in root)
#app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Serve index.html at /
# @app.get("/")
# def read_index():
#     return FileResponse(os.path.abspath("index.html"))

@app.get("/")
def read_index():
    index_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    return FileResponse(index_path)
    #return FileResponse(os.path.abspath("index.html"))

class SearchRequest(BaseModel):
    country: str
    query: str

class AiSuggestRequest(BaseModel):
    #results: list
    results: List[Dict[str, Any]]



@app.post("/search-price")
def search_price(request: SearchRequest):
    try:
        print("Received request:", request)
        results = []
        session = requests.Session()
        if request.country.upper() == "US":
            # Amazon
            try:
                amazon_results = scrape_amazon_us_bs4(request.query)
                print("Amazon scraper results:", amazon_results)
                results.extend(amazon_results)
            except Exception as e:
                print("Amazon scraper error:")
                traceback.print_exc()
            time.sleep(2)

            # Walmart
            try:
                walmart_results = scrape_walmart_us(request.query, session=session)
                print("Walmart scraper results:", walmart_results)
                results.extend(walmart_results)
            except Exception as e:
                print("Walmart scraper error:")
                traceback.print_exc()
            time.sleep(2)

            # BestBuy
            try:
                bestbuy_results = scrape_bestbuy_us(request.query, session=session)
                print("BestBuy scraper results:", bestbuy_results)
                results.extend(bestbuy_results)
            except Exception as e:
                print("BestBuy scraper error:")
                traceback.print_exc()
            time.sleep(2)

            # Target
            try:
                target_results = scrape_target_us(request.query, session=session)
                print("Target scraper results:", target_results)
                results.extend(target_results)
            except Exception as e:
                print("Target scraper error:")
                traceback.print_exc()

            return {"results": results}
        
        elif request.country.upper() == "IN":
            # Flipkart
            try:
                flipkart_results = scrape_flipkart_in(request.query, session=session)
                print("Flipkart scraper results:", flipkart_results)
                results.extend(flipkart_results)
            except Exception:
                print("Flipkart scraper error:")
                traceback.print_exc()
            return {"results": results}

        else:
            return {"error": "Country not supported"}
    except Exception as e:
        print("ERROR:", e)
        traceback.print_exc()
        return {"error": str(e)}

#OpenAI endpoint  
#OPENAI_API_KEY = ""
#openai.api_key = OPENAI_API_KEY

#(Demo AI Suggestion – no real LLM used in this version)
@app.post("/ai-suggest")
async def ai_suggest(request: AiSuggestRequest):
    results = request.results
    if not results:
        return {"suggestion": "No results to analyze."}
    # Pick the item with the lowest price
    def get_price(item):
        try:
            return float(item.get("price", "1e9"))
        except Exception:
            return 1e9
    best = min(results, key=get_price)
    suggestion = (
        f"Product: {best.get('productName', '')}\n"
        f"Price: {best.get('price', '')} {best.get('currency', '')}\n"
        f"AI Suggestion: This product appears to offer the best value for money based on price."
    )
    return {"suggestion": suggestion}

# @app.post("/ai-suggest")
# async def ai_suggest(request: AiSuggestRequest):
#     results = request.results
# #async def ai_suggest(request: Request):
#     #data = await request.json()
#     results = data.get("results", [])
#     if not results:
#         return {"suggestion": "No results to analyze."}
#     prompt = "Given this product list, which is the best value for money (briefly explain)?\n"
#     for i, r in enumerate(results, 1):
#         prompt += f"{i}. {r.get('productName', '')} - {r.get('price', '')} {r.get('currency', '')}\n"
#     prompt += "\nRespond with the product number, name, and a brief reason."
#     try:
#         completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             max_tokens=60,
#             temperature=0.2
#         )
#         suggestion = completion.choices[0].message.content.strip()
#         return {"suggestion": suggestion}
#     except Exception as e:
#         print("OpenAI error:", e)
#         return {"suggestion": "AI error: Could not generate suggestion."}
