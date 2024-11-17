from data_scraping.uci_scraping import scrape_uci_datasets

scrape_uci_datasets()
data = scrape_uci_datasets.data
jsondata = {data[0][i]: [data[j][i] for j in range(1, len(data))] for i in range(len(data[0]))}
