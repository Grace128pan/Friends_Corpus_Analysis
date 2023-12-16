import os
import requests
from bs4 import BeautifulSoup

# Base URLs for each season
base_urls = {
    "season4": "https://subslikescript.com/series/Friends-108778/season-4",
    "season5": "https://subslikescript.com/series/Friends-108778/season-5",
    "season6": "https://subslikescript.com/series/Friends-108778/season-6",
    "season7": "https://subslikescript.com/series/Friends-108778/season-7",
    "season8": "https://subslikescript.com/series/Friends-108778/season-8",
}

# Episode titles for each season
season_episode_titles = {
    "season4": [
        "The_One_with_the_Jellyfish",
        "The_One_with_the_Cat",
        "The_One_with_the_Cuffs",
        "The_One_with_the_Ballroom_Dancing",
        "The_One_with_Joeys_New_Girlfriend",
        "The_One_with_the_Dirty_Girl",
        "The_One_Where_Chandler_Crosses_the_Line",
        "The_One_with_Chandler_in_a_Box",
        "The_One_Where_Theyre_Going_to_Party",
        "The_One_with_the_Girl_from_Poughkeepsie",
        "The_One_with_Phobes_Uterus",
        "The_One_with_the_Embryos",
        "The_One_with_Rachels_Crush",
        "The_One_with_Joeys_Dirty_Day",
        "The_One_with_All_the_Rugby",
        "The_One_with_the_Fake_Party",
        "The_One_with_the_Free_Porn",
        "The_One_with_Rachels_New_Dress",
        "The_One_with_All_the_Haste",
        "The_One_with_All_the_Wedding_Dresses",
        "The_One_with_the_Invitation",
        "The_One_with_the_Worst_Best_Man_Ever",
        "The_One_with_Rosss_Wedding_Part_One",
        "The_One_with_Rosss_Wedding_Part_Two",
    ],
    "season5": [
        "The_One_After_Ross_Says_Rachel",
        "The_One_with_All_the_Kissing",
        "The_One_Hundredth",
        "The_One_Where_Phoebe_Hates_PBS",
        "The_One_with_the_Kips",
        "The_One_with_the_Yeti",
        "The_One_Where_Ross_Moves_In",
        "The_One_with_All_the_Thanksgivings",
        "The_One_with_Rosss_Sandwich",
        "The_One_with_the_Inappropriate_Sister",
        "The_One_with_All_the_Resolutions",
        "The_One_with_Chandler's_Work_Laugh",
        "The_One_with_Joeys_Bag",
        "The_One_Where_Everybody_Finds_Out",
        "The_One_with_the_Girl_Who_Hits_Joey",
        "The_One_with_the_Cop",
        "The_One_with_Rachels_Inadvertent_Kiss",
        "The_One_Where_Rachel_Smokes",
        "The_One_Where_Ross_Cant_Flirt",
        "The_One_with_the_Ride_Along",
        "The_One_with_the_Ball",
        "The_One_with_Joeys_Big_Break",
        "The_One_in_Vegas_Part_One",
        "The_One_in_Vegas_Part_Two",
    ],
    "season6": [
        "The_One_After_Vegas",
        "The_One_Where_Ross_Hugs_Rachel",
        "The_One_with_Rosss_Denial",
        "The_One_Where_Joey_Loses_His_Insurance",
        "The_One_with_Joeys_Porsche",
        "The_One_on_the_Last_Night",
        "The_One_Where_Phoebe_Runs",
        "The_One_with_Ross_Teeth",
        "The_One_Where_Ross_Got_High",
        "The_One_with_the_Routine",
        "The_One_with_the_Apothecary_Table",
        "The_One_with_the_Joke",
        "The_One_with_Rachels_Sister",
        "The_One_Where_Chandler_Cant_Cry",
        "The_One_That_Could_Have_Been_Part_One",
        "The_One_That_Could_Have_Been_Part_Two",
        "The_One_with_Unagi",
        "The_One_Where_Ross_Dates_a_Student",
        "The_One_with_Joeys_Fridge",
        "The_One_with_Mac_and_CHEESE",
        "The_One_Where_Ross_Meets_Elizabeths_Dad",
        "The_One_Where_Pauls_the_Man",
        "The_One_with_the_Ring",
        "The_One_with_the_Proposal_Part_One",
        "The_One_with_the_Proposal_Part_Two",
    ],
    "season7": [
        "The_One_with_Monicas_Thunder",
        "The_One_with_Rachels_Book",
        "The_One_with_Phobes_Cookies",
        "The_One_with_Rachels_Assistant",
        "The_One_with_the_Engagement_Picture",
        "The_One_with_the_Nap_Partners",
        "The_One_with_Rosss_Library_Book",
        "The_One_Where_Chandler_Doesnt_Like_Dogs",
        "The_One_with_All_the_Candy",
        "The_One_with_the_Holiday_Armadillo",
        "The_One_with_All_the_Cheesecakes",
        "The_One_Where_Theyre_Up_All_Night",
        "The_One_Where_Rosita_Dies",
        "The_One_Where_They_All_Turn_Thirty",
        "The_One_with_Joeys_New_Brain",
        "The_One_with_the_Truth_About_London",
        "The_One_with_the_Cheap_Wedding_Dress",
        "The_One_with_Joeys_Award",
        "The_One_with_Ross_and_Monicas_Cousin",
        "The_One_with_Rachels_Big_Kiss",
        "The_One_with_the_Vows",
        "The_One_with_Chandler's_Dad",
        "The_One_with_Monica_and_Chandler's_Wedding_Part_One",
        "The_One_with_Monica_and_Chandler's_Wedding_Part_Two",
    ],
    "season8": [
        "The_One_After_I_Do",
        "The_One_with_the_Red_Sweater",
        "The_One_Where_Rachel_Tells",
        "The_One_with_the_Videotape",
        "The_One_with_Rachels_Date",
        "The_One_with_the_Halloween_Party",
        "The_One_with_the_Stain",
        "The_One_with_the_Stripper",
        "The_One_with_the_Rumor",
        "The_One_with_Monicas_Boots",
        "The_One_with_Rosss_Step_Forward",
        "The_One_Where_Joey_Dates_Rachel",
        "The_One_Where_Chandler_Takes_a_Bath",
        "The_One_with_the_Secret_Closet",
        "The_One_with_the_Birthing_Video",
        "The_One_Where_Joey_Tells_Rachel",
        "The_One_with_the_Tea_Leaves",
        "The_One_in_Massapequa",
        "The_One_with_Joeys_Interview",
        "The_One_with_the_Baby_Shower",
        "The_One_with_the_Cooking_Class",
        "The_One_Where_Rachel_Is_Late",
        "The_One_Where_Rachel_Has_a_Baby_Part_One",
        "The_One_Where_Rachel_Has_a_Baby_Part_Two",
    ],
}


# Function to get the script for a given episode
def get_episode_script(season, episode_title):
    episode_url = f"{base_urls[season]}/episode-{season_episode_titles[season].index(episode_title) + 1}-{episode_title}"
    headers = {'Accept-Language': 'en-US,en;q=0.5'}
    response = requests.get(episode_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('div', {'class': 'full-script'}).get_text(separator='\n')
        return script
    else:
        return None


# Function to save scripts to individual text files
def save_scripts(season, scripts_folder):
    for title in season_episode_titles[season]:
        script = get_episode_script(season, title)
        if script:
            file_path = os.path.join(scripts_folder, f"{season}_{title}.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(script)
            print(f"Script for {title} (Season {season}) saved to {file_path}")
        else:
            print(f"Failed to retrieve script for {title} (Season {season})")


# Create folders for each season on the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
for season in base_urls.keys():
    scripts_folder = os.path.join(desktop_path, f"FriendsScripts{season[-1]}")
    os.makedirs(scripts_folder, exist_ok=True)
    save_scripts(season, scripts_folder)

print("All scripts have been saved.")
