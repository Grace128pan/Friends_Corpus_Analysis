import requests
from bs4 import BeautifulSoup
import os


# Function to get content and save to file
def get_and_save_content(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text content
        page_content = soup.get_text()

        # Specify the file path on your desktop
        file_path = os.path.join(os.path.expanduser("~"), "Desktop", file_name)

        # Write content to a text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(page_content)

        print(f"Content has been saved to {file_path}")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")


# Define Season 9, Episode 23-24 title and URL
episode_title_23_24 = "Episode 923-924: The One In Barbados"
episode_url_23_24 = "https://www.livesinabox.com/friends/season9/0923-0924.html"

# Modify title to create a valid file name
file_name_23_24 = f"{episode_title_23_24.replace(':', ' -')}.txt"

# Fetch content for Season 9, Episode 23-24 and save to file
get_and_save_content(episode_url_23_24, file_name_23_24)
