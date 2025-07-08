from app.scraper.amazon_us import scrape_amazon_us_sync

if __name__ == "__main__":
    results = scrape_amazon_us_sync("iPhone 16 Pro, 128GB")
    print(results)
