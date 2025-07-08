import requests

def scrape_amazon_us_bs4(query):
    # Use Fake Store API instead of Amazon, for testing.
    url = "https://fakestoreapi.com/products"
    resp = requests.get(url, timeout=10)
    data = resp.json()
    query_lower = query.lower()
    # Filter results based on query in title
    results = []
    for item in data:
        if query_lower in item['title'].lower():
            results.append({
                "productName": item['title'],
                "link": f"https://fakestoreapi.com/products/{item['id']}",
                "price": str(item['price']),
                "currency": "USD",
            })
        if len(results) >= 5:
            break
    # If nothing matched, just return top 5 products for demo
    if not results:
        for item in data[:5]:
            results.append({
                "productName": item['title'],
                "link": f"https://fakestoreapi.com/products/{item['id']}",
                "price": str(item['price']),
                "currency": "USD",
            })
    return results
