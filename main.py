#Import Necessary Libraries
import requests
from bs4 import BeautifulSoup
import csv

#Define the Base URL and CSV Headers
def scrape_uci_datasets():
    base_url = "https://archive.ics.uci.edu/datasets"


    headers = [
        "Dataset Name", "Donated Date", "Description",
        "Dataset Characteristics", "Subject Area", "Associated Tasks",
        "Feature Type", "Instances", "Features"
    ]


    data = []

    # Create a Function to Scrape Dataset Details
    def scrape_dataset_details(dataset_url):
        response = requests.get(dataset_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_name = soup.find(
            'h1', class_='text-3xl font-semibold text-primary-content')
        dataset_name = dataset_name.text.strip() if dataset_name else "N/A"


        donated_date = soup.find('h2', class_='text-sm text-primary-content')
        donated_date = donated_date.text.strip().replace(
            'Donated on ', '') if donated_date else "N/A"


        description = soup.find('p', class_='svelte-17wf9gp')
        description = description.text.strip() if description else "N/A"


        details = soup.find_all('div', class_='col-span-4')


        dataset_characteristics = details[0].find('p').text.strip() if len(
            details) > 0 else "N/A"
        subject_area = details[1].find('p').text.strip() if len(
            details) > 1 else "N/A"
        associated_tasks = details[2].find('p').text.strip() if len(
            details) > 2 else "N/A"
        feature_type = details[3].find('p').text.strip() if len(
            details) > 3 else "N/A"
        instances = details[4].find('p').text.strip() if len(
            details) > 4 else "N/A"
        features = details[5].find('p').text.strip() if len(
            details) > 5 else "N/A"


        return [
            dataset_name, donated_date, description, dataset_characteristics,
            subject_area, associated_tasks, feature_type, instances, features
        ]

    # Create a Function to Scrape Dataset Listings
    def scrape_datasets(page_url):
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_list = soup.find_all(
            'a', class_='link-hover link text-xl font-semibold')


        if not dataset_list:
            print("No dataset links found")
            return


        for dataset in dataset_list:
            dataset_link = "https://archive.ics.uci.edu" + dataset['href']
            print(f"Scraping details for {dataset.text.strip()}...")
            dataset_details = scrape_dataset_details(dataset_link)
            data.append(dataset_details)
        
    # Loop Through Pages Using Pagination Parameters
    skip = 0
    take = 10
    while True:
        page_url = f"https://archive.ics.uci.edu/datasets?skip={skip}&take={take}&sort=desc&orderBy=NumHits&search="
        print(f"Scraping page: {page_url}")
        initial_data_count = len(data)
        scrape_datasets(page_url)
        if len(
                data
        ) == initial_data_count:  
            break
        skip += take    

    # Save the Scraped Data to a CSV File
    with open('uci_datasets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


    print("Scraping complete. Data saved to 'uci_datasets.csv'.")

    # scrape_datasets("https://archive.ics.uci.edu/datasets")
    # return(data)

scrape_uci_datasets()
