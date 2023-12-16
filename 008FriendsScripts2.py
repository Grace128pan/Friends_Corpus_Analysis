import os
import requests
from bs4 import BeautifulSoup

base_url_season2 = "https://subslikescript.com/series/Friends-108778/season-2"

# List of episode titles for Season 2
season2_episode_titles = [
    "The_One_with_Rosss_New_Girlfriend",
    "The_One_with_the_Breast_Milk",
    "The_One_Where_Heckles_Dies",
    "The_One_with_Phoebes_Husband",
    "The_One_with_Five_Steaks_and_an_Eggplant",
    "The_One_with_the_Baby_on_the_Bus",
    "The_One_Where_Ross_Finds_Out",
    "The_One_with_the_List",
    "The_One_with_Phoebes_Dad",
    "The_One_with_Russ",
    "The_One_with_the_Lesbian_Wedding",
    "The_One_After_the_Superbowl_Part_1",
    "The_One_After_the_Superbowl_Part_2",
    "The_One_with_the_Prom_Video",
    "The_One_Where_Ross_and_Rachel_You_Know",
    "The_One_Where_Joey_Moves_Out",
    "The_One_Where_Eddie_Moves_In",
    "The_One_Where_Dr_Ramoray_Dies",
    "The_One_Where_Eddie_Wont_Go",
    "The_One_Where_Old_Yeller_Dies",
    "The_One_with_the_Bullies",
    "The_One_with_the_Two_Parties",
    "The_One_with_the_Chicken_Pox",
    "The_One_with_Barry_and_Mindys_Wedding",
]

# Replace "YOUR_DESKTOP_PATH" with the actual path to your desktop
output_directory = r"C:\Users\Grace\Desktop\FriendsScripts2"

os.makedirs(output_directory, exist_ok=True)


# Function to get the script for a given episode
def get_episode_script(episode_title):
    episode_url = f"{base_url_season2}/episode-{season2_episode_titles.index(episode_title) + 1}-{episode_title}"
    headers = {'Accept-Language': 'en-US,en;q=0.5'}
    response = requests.get(episode_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('div', {'class': 'full-script'}).get_text(separator='\n')
        return script
    else:
        return None


# Save each episode script to a separate text file for Season 2
for title in season2_episode_titles:
    script = get_episode_script(title)
    if script:
        file_path = os.path.join(output_directory, f"{season2_episode_titles.index(title) + 1}_{title}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(script)
        print(f"Script for {title} (Season 2) saved to {file_path}")
    else:
        print(f"Failed to retrieve script for {title} (Season 2)")

print("All scripts for Season 2 have been saved.")

