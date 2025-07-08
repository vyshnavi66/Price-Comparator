def scrape_walmart_us(query, session=None):
    # Demo/mock data for Walmart (always returns results)
    return [
        {
            "productName": "Ozark Trail 32oz Water Bottle",
            "price": "10.99",
            "currency": "USD",
            "link": "https://www.walmart.com/ip/12345678"
        },
        {
            "productName": "Great Value Distilled Water, 1 Gal",
            "price": "1.18",
            "currency": "USD",
            "link": "https://www.walmart.com/ip/87654321"
        }
    ]
