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


# Define Season 5 episode titles and corresponding URLs
season5_episode_titles = [
    "Episode 501: The One After Ross Says Rachel",
    "Episode 502: The One With All The Kissing",
    "Episode 503: The One Hundredth",
    "Episode 504: The One Where Phoebe Hates PBS",
    "Episode 505: The One With All the Kips",
    "Episode 506: The One With The Yeti",
    "Episode 507: The One Where Ross Moves In",
    "Episode 508: The One With The Thanksgiving Flashbacks",
    "Episode 509: The One With Ross's Sandwich",
    "Episode 510: The One With The Inappropriate Sister",
    "Episode 511: The One With All The Resolutions",
    "Episode 512: The One With Chandler's Work Laugh",
    "Episode 513: The One With Joey's Bag",
    "Episode 514: The One Where Everyone Finds Out",
    "Episode 515: The One With The Girl Who Hits Joey",
    "Episode 516: The One With A Cop",
    "Episode 517: The One With Rachel's Inadvertent Kiss",
    "Episode 518: The One Where Rachel Smokes",
    "Episode 519: The One Where Ross Can't Flirt",
    "Episode 520: The One With The Ride Along",
    "Episode 521: The One With The Ball",
    "Episode 522: The One With Joey's Big Break",
    "Episode 523: The One In Vegas"
]

season5_episode_urls = [
    "https://www.livesinabox.com/friends/season5/501arsr.htm",
    "https://www.livesinabox.com/friends/season5/502kiss.htm",
    "https://www.livesinabox.com/friends/season5/503t100.htm",
    "https://www.livesinabox.com/friends/season5/504pbs.htm",
    "https://www.livesinabox.com/friends/season5/505kips.htm",
    "https://www.livesinabox.com/friends/season5/506yeti.htm",
    "https://www.livesinabox.com/friends/season5/507rmi.htm",
    "https://www.livesinabox.com/friends/season5/508towtf.htm",
    "https://www.livesinabox.com/friends/season5/509towrs.htm",
    "https://www.livesinabox.com/friends/season5/510towas.htm",
    "https://www.livesinabox.com/friends/season5/511towr.htm",
    "https://www.livesinabox.com/friends/season5/512cwl.htm",
    "https://www.livesinabox.com/friends/season5/513bag.htm",
    "https://www.livesinabox.com/friends/season5/514efo.htm",
    "https://www.livesinabox.com/friends/season5/515ghj.htm",
    "https://www.livesinabox.com/friends/season5/516cop.htm",
    "https://www.livesinabox.com/friends/season5/517rik.htm",
    "https://www.livesinabox.com/friends/season5/518towrs.htm",
    "https://www.livesinabox.com/friends/season5/519rcf.htm",
    "https://www.livesinabox.com/friends/season5/520tra.htm",
    "https://www.livesinabox.com/friends/season5/521ball.htm",
    "https://www.livesinabox.com/friends/season5/522jbb.htm",
    "https://www.livesinabox.com/friends/season5/523toiv.htm"
]

# Loop through Season 5 episodes and fetch content
for title, url in zip(season5_episode_titles, season5_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
