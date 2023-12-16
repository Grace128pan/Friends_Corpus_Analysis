import os
import requests
from bs4 import BeautifulSoup

# Create a folder for storing scripts
folder_name = "FriendsScripts9"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
scripts_folder_path = os.path.join(desktop_path, folder_name)

if not os.path.exists(scripts_folder_path):
    os.makedirs(scripts_folder_path)

# URLs for each episode
episode_urls = [
    "https://subslikescript.com/series/Friends-108778/season-9/episode-1-The_One_Where_No_One_Proposes",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-2-The_One_Where_Emma_Cries",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-3-The_One_with_the_Pediatrician",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-4-The_One_with_the_Sharks",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-5-The_One_with_Phoebe's_Birthday_Dinner",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-6-The_One_with_the_Male_Nanny",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-7-The_One_with_Ross's_Inappropriate_Song",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-8-The_One_with_Rachel's_Other_Sister",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-9-The_One_with_Rachel's_Phone_Number",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-10-The_One_with_Christmas_in_Tulsa",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-11-The_One_Where_Rachel_Goes_Back_to_Work",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-12-The_One_with_Phoebe's_Rats",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-13-The_One_Where_Monica_Sings",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-14-The_One_with_the_Blind_Dates",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-15-The_One_with_the_Mugging",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-16-The_One_with_the_Boob_Job",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-17-The_One_with_the_Memorial_Service",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-18-The_One_with_the_Lottery",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-19-The_One_with_Rachel's_Dream",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-20-The_One_with_the_Soap_Opera_Party",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-21-The_One_with_the_Fertility_Test",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-22-The_One_with_the_Donor",
    "https://subslikescript.com/series/Friends-108778/season-9/episode-23-The_One_in_Barbados_Part_1",
]

# Iterate through each episode
for i, episode_url in enumerate(episode_urls, start=1):
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

print("All scripts have been saved successfully.")


