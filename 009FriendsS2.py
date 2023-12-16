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


# Define Season 2 episode titles and corresponding URLs
season2_episode_titles = [
    "Episode 201: The One With Ross's New Girlfriend",
    "Episode 202: The One With The Breast Milk",
    "Episode 203: The One Where Heckles Dies",
    "Episode 204: The One With Phoebe's Husband",
    "Episode 205: The One With Five Steaks and an Eggplant",
    "Episode 206: The One With The Baby On the Bus",
    "Episode 207: The One Where Ross Finds Out",
    "Episode 208: The One With The List",
    "Episode 209: The One With Phoebe's Dad",
    "Episode 210: The One With Russ",
    "Episode 211: The One With The Lesbian Wedding",
    "Episode 212: The One After the Superbowl",
    "Episode 214: The One With The Prom Video",
    "Episode 215: The One Where Ross and Rachel...You Know",
    "Episode 216: The One Where Joey Moves Out",
    "Episode 217: The One Where Eddie Moves In",
    "Episode 218: The One Where Dr. Remoray Dies",
    "Episode 219: The One Where Eddie Won't Go",
    "Episode 220: The One Where Old Yeller Dies",
    "Episode 221: The One With The Bullies",
    "Episode 222: The One With The Two Parties",
    "Episode 223: The One With The Chicken Pox",
    "Episode 224: The One With Barry and Mindy's Wedding"
]

season2_episode_urls = [
    "https://www.livesinabox.com/friends/season2/201rng.htm",
    "https://www.livesinabox.com/friends/season2/202brst.htm",
    "https://www.livesinabox.com/friends/season2/203towhd.htm",
    "https://www.livesinabox.com/friends/season2/204towph.htm",
    "https://www.livesinabox.com/friends/season2/205fsae.htm",
    "https://www.livesinabox.com/friends/season2/206baby.htm",
    "https://www.livesinabox.com/friends/season2/207rofo.htm",
    "https://www.livesinabox.com/friends/season2/208list.htm",
    "https://www.livesinabox.com/friends/season2/209towpd.htm",
    "https://www.livesinabox.com/friends/season2/210russ.htm",
    "https://www.livesinabox.com/friends/season2/211towlw.htm",
    "https://www.livesinabox.com/friends/season2/212toasb.htm",
    "https://www.livesinabox.com/friends/season2/214towpv.htm",
    "https://www.livesinabox.com/friends/season2/215rryk.htm",
    "https://www.livesinabox.com/friends/season2/216jmo.htm",
    "https://www.livesinabox.com/friends/season2/217emi.htm",
    "https://www.livesinabox.com/friends/season2/218drd.htm",
    "https://www.livesinabox.com/friends/season2/219ewg.htm",
    "https://www.livesinabox.com/friends/season2/220oyd.htm",
    "https://www.livesinabox.com/friends/season2/221towtb.htm",
    "https://www.livesinabox.com/friends/season2/222towtp.htm",
    "https://www.livesinabox.com/friends/season2/223towcp.htm",
    "https://www.livesinabox.com/friends/season2/224bamw.htm"
]

# Loop through Season 2 episodes and fetch content
for title, url in zip(season2_episode_titles, season2_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
