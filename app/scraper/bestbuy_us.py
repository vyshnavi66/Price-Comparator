def scrape_bestbuy_us(query, session=None):
    # Demo/mock data for BestBuy (always returns results)
    return [
        {
            "productName": "Insignia™ - 32\" Class F20 Series LED HD Smart Fire TV",
            "price": "99.99",
            "currency": "USD",
            "link": "https://www.bestbuy.com/site/123456"
        },
        {
            "productName": "Apple MacBook Air 13.3\" Laptop - M1 Chip, 8GB Memory",
            "price": "849.99",
            "currency": "USD",
            "link": "https://www.bestbuy.com/site/234567"
        }
    ]
