import os
import requests
from bs4 import BeautifulSoup

# Function to scrape and save script for a given URL and file name
def scrape_and_save_script(url, file_name):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element containing the script
        script_element = soup.find('div', class_='full-script')

        # Extract the text content of the script
        script_text = script_element.get_text(separator='\n')

        # Define the folder and file names
        folder_name = "FriendsScripts7"

        # Create the folder if it doesn't exist
        os.makedirs(folder_name, exist_ok=True)

        # Define the full file path
        file_path = os.path.join(folder_name, file_name)

        # Write the script to a text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(script_text)

        print(f"Script for {file_name} has been successfully scraped and saved to: {file_path}")

    else:
        print(f"Failed to retrieve the content for {file_name}. Status code: {response.status_code}")

# URLs for the specified episodes
episode3_url = "https://subslikescript.com/series/Friends-108778/season-7/episode-3-The_One_with_Phoebes_Cookies"
episode22_url = "https://subslikescript.com/series/Friends-108778/season-7/episode-22-The_One_with_Chandlers_Dad"
episode23_url = "https://subslikescript.com/series/Friends-108778/season-7/episode-23-The_One_with_Monica_and_Chandlers_Wedding_Part_1"
episode24_url = "https://subslikescript.com/series/Friends-108778/season-7/episode-24-The_One_with_Monica_and_Chandlers_Wedding_Part_2"

# File names for each episode
episode3_file_name = "3.season7 The_One_with_Phoebes_Cookies.txt"
episode22_file_name = "22.season7 The_One_with_Chandlers_Dad.txt"
episode23_file_name = "23.season7 The_One_with_Monica_and_Chandlers_Wedding_Part_1.txt"
episode24_file_name = "24.season7 The_One_with_Monica_and_Chandlers_Wedding_Part_2.txt"

# Scrape and save scripts for each episode
scrape_and_save_script(episode3_url, episode3_file_name)
scrape_and_save_script(episode22_url, episode22_file_name)
scrape_and_save_script(episode23_url, episode23_file_name)
scrape_and_save_script(episode24_url, episode24_file_name)
