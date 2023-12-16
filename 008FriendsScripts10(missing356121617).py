import os
import requests
from bs4 import BeautifulSoup

# Create a folder for storing scripts
folder_name = "MissingFriendsS10"
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Specify episode URLs
episode_urls = [
    "https://subslikescript.com/series/Friends-108778/season-10/episode-3-The_One_with_Rosss_Tan",
    "https://subslikescript.com/series/Friends-108778/season-10/episode-5-The_One_Where_Rachels_Sister_Babysits",
    "https://subslikescript.com/series/Friends-108778/season-10/episode-6-The_One_with_Ross_Grant",
    "https://subslikescript.com/series/Friends-108778/season-10/episode-12-The_One_with_Phoebes_Wedding",
    "https://subslikescript.com/series/Friends-108778/season-10/episode-16-The_One_with_Rachels_Going_Away_Party",
    "https://subslikescript.com/series/Friends-108778/season-10/episode-17-The_Last_One_Part_1",
]

# Iterate through episode URLs, fetch script, and save to text file
for episode_url in episode_urls:
    episode_page = requests.get(episode_url)
    episode_soup = BeautifulSoup(episode_page.content, 'html.parser')

    # Extract script content
    script_div = episode_soup.find("div", {"class": "full-script"})
    script_text = script_div.get_text(separator='\n') if script_div else "Script not available."

    # Extract season and episode number from URL
    season_number = episode_url.split('/')[-3].split('-')[-1]
    episode_number = episode_url.split('/')[-1].split('-')[-1]

    # Extract episode title
    episode_title_element = episode_soup.find("h1", {"class": "title"})
    episode_title = episode_title_element.text.strip() if episode_title_element else "Unknown Episode Title"

    # Save to a text file
    file_name = f"{season_number}_E{episode_number}_{episode_title.replace(' ', '_')}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_text)

print("Scripts have been successfully saved to the MissingFriendsS10 folder on your desktop.")
