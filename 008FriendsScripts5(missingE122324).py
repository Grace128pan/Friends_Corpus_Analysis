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
        folder_name = "FriendsScripts5"

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
episode12_url = "https://subslikescript.com/series/Friends-108778/season-5/episode-12-The_One_with_Chandlers_Work_Laugh"
episode23_url = "https://subslikescript.com/series/Friends-108778/season-5/episode-23-The_One_in_Vegas_Part_1"
episode24_url = "https://subslikescript.com/series/Friends-108778/season-5/episode-24-The_One_in_Vegas_Part_2"

# File names for each episode
episode12_file_name = "12.season5 The_One_with_Chandlers_Work_Laugh.txt"
episode23_file_name = "23.season5 The_One_in_Vegas_Part_1.txt"
episode24_file_name = "24.season5 The_One_in_Vegas_Part_2.txt"

# Scrape and save scripts for each episode
scrape_and_save_script(episode12_url, episode12_file_name)
scrape_and_save_script(episode23_url, episode23_file_name)
scrape_and_save_script(episode24_url, episode24_file_name)
