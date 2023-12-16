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


# Define episode titles and corresponding URLs
episode_titles = [
    "Episode 101: The Pilot-The Uncut Version",
    "Episode 102: The One With The Sonogram At the End",
    "Episode 103: The One With The Thumb",
    "Episode 104: The One With George Stephanopoulos",
    "Episode 105: The One With The East German Laundry Detergent",
    "Episode 106: The One With The Butt",
    "Episode 107: The One With The Blackout",
    "Episode 108: The One Where Nana Dies Twice",
    "Episode 109: The One Where Underdog Gets Away",
    "Episode 110: The One With The Monkey",
    "Episode 111: The One With Mrs. Bing",
    "Episode 112: The One With The Dozen Lasagnas",
    "Episode 113: The One With The Boobies",
    "Episode 114: The One With The Candy Hearts",
    "Episode 115: The One With The Stoned Guy",
    "Episode 116: The One With Two Parts: Part One",
    "Episode 117: The One With Two Parts: Part Two",
    "Episode 118: The One With All The Poker",
    "Episode 119: The One Where The Monkey Gets Away",
    "Episode 120: The One With The Evil Orthodontist",
    "Episode 121: The One With The Fake Monica",
    "Episode 122: The One With The Ick Factor",
    "Episode 123: The One With The Birth",
    "Episode 124: The One Where Rachel Finds Out"
]

episode_urls = [
    "https://www.livesinabox.com/friends/season1/101pilot.htm",
    "https://www.livesinabox.com/friends/season1/102towsg.htm",
    "https://www.livesinabox.com/friends/season1/103thumb.htm",
    "https://www.livesinabox.com/friends/season1/104towgs.htm",
    "https://www.livesinabox.com/friends/season1/105egld.htm",
    "https://www.livesinabox.com/friends/season1/106butt.htm",
    "https://www.livesinabox.com/friends/season1/107towbo.htm",
    "https://www.livesinabox.com/friends/season1/108ndt.htm",
    "https://www.livesinabox.com/friends/season1/109uga.htm",
    "https://www.livesinabox.com/friends/season1/110monk.htm",
    "https://www.livesinabox.com/friends/season1/111mbing.htm",
    "https://www.livesinabox.com/friends/season1/112towdl.htm",
    "https://www.livesinabox.com/friends/season1/113tits.htm",
    "https://www.livesinabox.com/friends/season1/114towch.htm",
    "https://www.livesinabox.com/friends/season1/115towsg.htm",
    "https://www.livesinabox.com/friends/season1/116part1.htm",
    "https://www.livesinabox.com/friends/season1/117part2.htm",
    "https://www.livesinabox.com/friends/season1/118poke.htm",
    "https://www.livesinabox.com/friends/season1/119mga.htm",
    "https://www.livesinabox.com/friends/season1/120toweo.htm",
    "https://www.livesinabox.com/friends/season1/121towfm.htm",
    "https://www.livesinabox.com/friends/season1/122ick.htm",
    "https://www.livesinabox.com/friends/season1/123birth.htm",
    "https://www.livesinabox.com/friends/season1/124rafo.htm"
]

# Loop through episodes and fetch content
for title, url in zip(episode_titles, episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
