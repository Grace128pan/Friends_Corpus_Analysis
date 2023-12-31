import os
import requests
from bs4 import BeautifulSoup

base_url = "https://subslikescript.com/series/Friends-108778"

# List of episode titles
episode_titles = [
    "The_One_Where_Monica_Gets_a_Roommate",
    "The_One_with_the_Sonogram_at_the_End",
    "The_One_with_the_Thumb",
    "The_One_with_George_Stephanopoulos",
    "The_One_with_the_East_German_Laundry_Detergent",
    "The_One_with_the_Butt",
    "The_One_with_the_Blackout",
    "The_One_Where_Nana_Dies_Twice",
    "The_One_Where_Underdog_Gets_Away",
    "The_One_with_the_Monkey",
    "The_One_with_Mrs_Bing",
    "The_One_with_the_Dozen_Lasagnas",
    "The_One_with_the_Boobies",
    "The_One_with_the_Candy_Hearts",
    "The_One_with_the_Stoned_Guy",
    "The_One_with_Two_Parts_Part_1",
    "The_One_with_Two_Parts_Part_2",
    "The_One_with_All_the_Poker",
    "The_One_Where_the_Monkey_Gets_Away",
    "The_One_with_the_Evil_Orthodontist",
    "The_One_with_the_Fake_Monica",
    "The_One_with_the_Ick_Factor",
    "The_One_with_the_Birth",
    "The_One_Where_Rachel_Finds_Out"
]

# Replace "YOUR_DESKTOP_PATH" with the actual path to your desktop
output_directory = r"C:\Users\Grace\Desktop\Friends_Episode_Scripts1"

os.makedirs(output_directory, exist_ok=True)


# Function to get the script for a given episode
def get_episode_script(title):
    episode_url = f"{base_url}/season-1/episode-{episode_titles.index(title) + 1}-{title}#google_vignette"
    response = requests.get(episode_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('div', {'class': 'full-script'}).get_text(separator='\n')
        return script
    else:
        return None


# Save each episode script to a separate text file
for title in episode_titles:
    script = get_episode_script(title)
    if script:
        file_path = os.path.join(output_directory, f"{title}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(script)
        print(f"Script for {title} saved to {file_path}")
    else:
        print(f"Failed to retrieve script for {title}")

print("All scripts have been saved.")






