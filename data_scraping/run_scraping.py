from uci_scraping import scrape_uci_datasets 

# Call the scraping task asynchronously
result = scrape_uci_datasets.delay()

# Wait for the result and print it
print(f"Task Result: {result.get(timeout=300)}")
