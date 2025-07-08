def scrape_target_us(query, session=None):
    # Demo/mock data for Target (always returns results)
    return [
        {
            "productName": "Contigo 24oz Water Bottle - Blue",
            "price": "12.99",
            "currency": "USD",
            "link": "https://www.target.com/p/contigo-24oz-water-bottle-blue/-/A-123456789"
        },
        {
            "productName": "Apple AirPods Pro (2nd Generation)",
            "price": "199.99",
            "currency": "USD",
            "link": "https://www.target.com/p/apple-airpods-pro-2nd-gen/-/A-7654321"
        }
    ]
