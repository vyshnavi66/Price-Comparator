from app.scraper.amazon_us import scrape_amazon_us
from app.scraper.flipkart_in import scrape_flipkart_in

def get_scrapers_by_country(country_code):
    country_map = {
        "US": [scrape_amazon_us],
        "IN": [scrape_flipkart_in],
        # Add more mappings here
    }
    return country_map.get(country_code.upper(), [])
