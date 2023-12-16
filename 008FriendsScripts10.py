import os
import requests
from bs4 import BeautifulSoup

# Create a folder for storing scripts
folder_name = "FriendsScripts10"
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# URL for the main page containing links to each episode
main_url = "https://subslikescript.com/series/Friends-108778"

# Fetch the main page content
main_page = requests.get(main_url)
main_soup = BeautifulSoup(main_page.content, 'html.parser')

# Extract episode URLs
episode_links = []
season_number = 10

for episode_number, episode_title in enumerate(
    [
        "The One After Joey and Rachel Kiss",
        "The One Where Ross Is Fine",
        "The One with Ross's Tan",
        "The One with the Cake",
        "The One Where Rachel's Sister Babysits",
        "The One with Ross' Grant",
        "The One with the Home Study",
        "The One with the Late Thanksgiving",
        "The One with the Birth Mother",
        "The One Where Chandler Gets Caught",
        "The One Where the Stripper Cries",
        "The One with Phoebe's Wedding",
        "The One Where Joey Speaks French",
        "The One with Princess Consuela",
        "The One Where Estelle Dies",
        "The One with Rachel's Going Away Party",
        "The Last One: Part 1",
    ],
    start=1,
):
    episode_url = f"{main_url}/season-{season_number}/episode-{episode_number}-{episode_title.replace(' ', '_')}"
    episode_links.append((episode_title, episode_url))

# Iterate through episode links, fetch script, and save to text file
for episode_title, episode_url in episode_links:
    episode_page = requests.get(episode_url)
    episode_soup = BeautifulSoup(episode_page.content, 'html.parser')

    # Extract script content
    script_div = episode_soup.find("div", {"class": "full-script"})
    script_text = script_div.get_text(separator='\n') if script_div else "Script not available."

    # Extract episode number
    episode_number = episode_url.split('/')[-1].split('-')[1]

    # Save to a text file
    file_name = f"{season_number}_E{episode_number}_{episode_title.replace(' ', '_')}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_text)

print("Scripts have been successfully saved to the FriendsScripts10 folder on your desktop.")
