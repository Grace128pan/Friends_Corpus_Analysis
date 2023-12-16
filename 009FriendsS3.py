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


# Define Season 3 episode titles and corresponding URLs
season3_episode_titles = [
    "Episode 301: The One With The Princess Leia Fantasy",
    "Episode 302: The One Where No One's Ready",
    "Episode 303: The One With All The Jam",
    "Episode 304: The One With The Metaphorical Tunnel",
    "Episode 305: The One With Frank Jr.",
    "Episode 306: The One With The Flashback",
    "Episode 307: The One With The Racecar Bed",
    "Episode 308: The One With The Giant Poking Device",
    "Episode 309: The One With The Football",
    "Episode 310: The One Where Rachel Quits",
    "Episode 311: The One Where Chandler Can't Remember Which Sister",
    "Episode 312: The One With All The Jealousy",
    "Episode 313: The One Where Monica And Richard Are Friends",
    "Episode 314: The One With Phoebe's Ex-Partner",
    "Episode 315: The One Where Ross and Rachel Take A Break",
    "Episode 316: The One The Morning After",
    "Episode 317: The One Without The Ski Trip",
    "Episode 318: The One With The Hypnosis Tape",
    "Episode 319: The One With The Tiny T-Shirt",
    "Episode 320: The One With The Dollhouse",
    "Episode 321: The One With A Chick. And A Duck",
    "Episode 322: The One With The Screamer",
    "Episode 323: The One With Ross's Thing",
    "Episode 324: The One With The Ultimate Fighting Championship",
    "Episode 325: The One At The Beach"
]

season3_episode_urls = [
    "https://www.livesinabox.com/friends/season3/301plf.htm",
    "https://www.livesinabox.com/friends/season3/302nor.htm",
    "https://www.livesinabox.com/friends/season3/303jam.htm",
    "https://www.livesinabox.com/friends/season3/304towmt.htm",
    "https://www.livesinabox.com/friends/season3/305frank.htm",
    "https://www.livesinabox.com/friends/season3/306flash.htm",
    "https://www.livesinabox.com/friends/season3/307rcb.htm",
    "https://www.livesinabox.com/friends/season3/308gpd.htm",
    "https://www.livesinabox.com/friends/season3/309towfb.htm",
    "https://www.livesinabox.com/friends/season3/310rquit.htm",
    "https://www.livesinabox.com/friends/season3/311crws.htm",
    "https://www.livesinabox.com/friends/season3/312towj.htm",
    "https://www.livesinabox.com/friends/season3/313maraf.htm",
    "https://www.livesinabox.com/friends/season3/314pexp.htm",
    "https://www.livesinabox.com/friends/season3/315rrtb.htm",
    "https://www.livesinabox.com/friends/season3/316toama.htm",
    "https://www.livesinabox.com/friends/season3/317towst.htm",
    "https://www.livesinabox.com/friends/season3/318towht.htm",
    "https://www.livesinabox.com/friends/season3/319tiny.htm",
    "https://www.livesinabox.com/friends/season3/320towdh.htm",
    "https://www.livesinabox.com/friends/season3/321pets.htm",
    "https://www.livesinabox.com/friends/season3/322screm.htm",
    "https://www.livesinabox.com/friends/season3/323towrt.htm",
    "https://www.livesinabox.com/friends/season3/324ufc.htm",
    "https://www.livesinabox.com/friends/season3/325toab.htm"
]

# Loop through Season 3 episodes and fetch content
for title, url in zip(season3_episode_titles, season3_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
