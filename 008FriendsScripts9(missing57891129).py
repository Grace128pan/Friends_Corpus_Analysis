import os
import requests
from bs4 import BeautifulSoup

# Create a folder for storing missing scripts
folder_name = "FriendsScripts9Missing"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
scripts_folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(scripts_folder_path):
    os.makedirs(scripts_folder_path)

# URLs for the missing episodes
missing_episode_urls = [
    "https://subslikescript.com/series/Friends-108778/season-9/episode-5-The_One_with_Phoebes_Birthday_Dinner",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-7-The_One_with_Rosss_Inappropriate_Song",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-8-The_One_with_Rachels_Other_Sister",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-9-The_One_with_Rachels_Phone_Number",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-12-The_One_with_Phoebes_Rats",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-19-The_One_with_Rachels_Dream",
]

# Iterate through each missing episode
for i, episode_url in enumerate(missing_episode_urls, start=1):
    # Fetch HTML content
    response = requests.get(episode_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the script content
    script_divs = soup.find_all('div', {'class': 'full-script'})
    script_content = "\n".join(div.get_text(separator='\n') for div in script_divs) if script_divs else "Script not available"

    # Create a txt file and write the script content
    episode_title = f"Episode_{i}_{episode_url.split('-')[-1]}"
    file_path = os.path.join(scripts_folder_path, f"{episode_title}.txt")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_content)

    print(f"Script for {episode_title} saved.")

print("All missing scripts have been saved successfully.")
