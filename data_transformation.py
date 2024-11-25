# from data_scraping.uci_scraping import scrape_uci_datasets
import pandas as pd

def csv_to_dicts():

    # data = scrape_uci_datasets() # Get the scraped data from the function

    data = pd.read_csv('/workspaces/UCI-Scraper/data_scraped/uci_datasets.csv')
    data_dicts =   data.to_dict(orient='records') # Convert the DataFrame to a list of dictionaries
    return data_dicts 