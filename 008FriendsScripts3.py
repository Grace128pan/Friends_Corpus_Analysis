import os
import requests
from bs4 import BeautifulSoup

base_url_season3 = "https://subslikescript.com/series/Friends-108778/season-3"

# List of episode titles for Season 3
season3_episode_titles = [
    "The_One_with_the_Princess_Leia_Fantasy",
    "The_One_Where_No_Ones_Ready",
    "The_One_with_the_Jam",
    "The_One_with_the_Metaphorical_Tunnel",
    "The_One_with_Frank_Jr",
    "The_One_with_the_Flashback",
    "The_One_with_the_Race_Car_Bed",
    "The_One_with_the_Giant_Poking_Device",
    "The_One_with_the_Football",
    "The_One_Where_Rachel_Quits",
    "The_One_Where_Chandler_Cant_Remember_Which_Sister",
    "The_One_with_All_the_Jealousy",
    "The_One_Where_Monica_and_Richard_Are_Just_Friends",
    "The_One_with_Phobes_Ex-Partner",
    "The_One_Where_Ross_and_Rachel_Take_a_Break",
    "The_One_the_Morning_After",
    "The_One_Without_the_Ski_Trip",
    "The_One_with_the_Hypnosis_Tape",
    "The_One_with_the_Tiny_T-Shirt",
    "The_One_with_the_Dollhouse",
    "The_One_with_the_Chick_and_the_Duck",
    "The_One_with_the_Screamer",
    "The_One_with_Rosss_Thing",
    "The_One_with_the_Ultimate_Fighting_Champion",
    "The_One_at_the_Beach",
]

# Replace "YOUR_DESKTOP_PATH" with the actual path to your desktop
output_directory = r"C:\Users\Grace\Desktop\FriendsScripts3"

os.makedirs(output_directory, exist_ok=True)


# Function to get the script for a given episode
def get_episode_script(episode_title):
    episode_url = f"{base_url_season3}/episode-{season3_episode_titles.index(episode_title) + 1}-{episode_title}"
    headers = {'Accept-Language': 'en-US,en;q=0.5'}
    response = requests.get(episode_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('div', {'class': 'full-script'}).get_text(separator='\n')
        return script
    else:
        return None


# Save each episode script to a separate text file for Season 3
for title in season3_episode_titles:
    script = get_episode_script(title)
    if script:
        file_path = os.path.join(output_directory, f"{season3_episode_titles.index(title) + 1}_{title}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(script)
        print(f"Script for {title} (Season 3) saved to {file_path}")
    else:
        print(f"Failed to retrieve script for {title} (Season 3)")

print("All scripts for Season 3 have been saved.")
