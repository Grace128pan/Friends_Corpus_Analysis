import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the Latvian website you want to scrape
url = 'http://valoda.ailab.lv/folklora/ticejumi/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the main content container
    content = soup.find('div', class_='archive-content')

    # Initialize empty lists to store the data
    data = []

    # Loop through the content and extract the information
    for entry in content.find_all('div', class_='entry'):
        chapter = entry.find('div', class_='chapter').text.strip()
        subchapter = entry.find('div', class_='subchapter').text.strip()
        unit = entry.find('div', class_='unit').text.strip()
        place = entry.find('div', class_='place').text.strip()
        comment = entry.find('div', class_='comment').text.strip() if entry.find('div', class_='comment') else ""

        data.append([chapter, subchapter, unit, place, comment])

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=['Chapter', 'Subchapter', 'Unit', 'Place', 'Comment'])

    # Save the DataFrame as a CSV file
    df.to_csv('folklore_data_latvian.csv', index=False)

    print("Data has been successfully scraped and saved to 'folklore_data_latvian.csv'.")

else:
    print("Failed to retrieve the web page.")



