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


# Define Season 7 episode titles and corresponding URLs
season7_episode_titles = [
    "Episode 701: The One With Monica's Thunder",
    "Episode 702: The One With Rachel's Book",
    "Episode 703: The One With Phoebe's Cookies",
    "Episode 704: The One With Rachel's Assistant",
    "Episode 705: The One With The Engagement Picture",
    "Episode 706: The One With The Nap Partners",
    "Episode 707: The One With Ross's Library Book",
    "Episode 708: The One Where Chandler Doesn't Like Dogs",
    "Episode 709: The One With All The Candy",
    "Episode 710: The One With The Christmas Armadilio",
    "Episode 711: The One With All The Cheesecakes",
    "Episode 712: The One Where They're Up All Night",
    "Episode 713: The One Where Rosita Dies",
    "Episode 714: The One Where They All Turn Thirty",
    "Episode 715: The One With Joey's New Brain",
    "Episode 716: The One With The Truth About London",
    "Episode 717: The One With The Cheap Wedding Dress",
    "Episode 718: The One With Joey's Award",
    "Episode 719: The One With Ross and Monica's Cousin",
    "Episode 720: The One With Rachel's Big Kiss",
    "Episode 721: The One With The Vows",
    "Episode 722: The One With Chandler's Dad",
    "Episode 723: The One With Monica and Chandler's Wedding",
    "Friends: The Stuff You've Never Seen"
]

season7_episode_urls = [
    "https://www.livesinabox.com/friends/season7/701towmt.htm",
    "https://www.livesinabox.com/friends/season7/702towrb.htm",
    "https://www.livesinabox.com/friends/season7/703towpc.htm",
    "https://www.livesinabox.com/friends/season7/704towra.htm",
    "https://www.livesinabox.com/friends/season7/705towep.htm",
    "https://www.livesinabox.com/friends/season7/706my100.htm",
    "https://www.livesinabox.com/friends/season7/707towrb.htm",
    "https://www.livesinabox.com/friends/season7/708cdld.htm",
    "https://www.livesinabox.com/friends/season7/709candy.htm",
    "https://www.livesinabox.com/friends/season7/710towha.htm",
    "https://www.livesinabox.com/friends/season7/711towcc.htm",
    "https://www.livesinabox.com/friends/season7/712tuan.htm",
    "https://www.livesinabox.com/friends/season7/713towrd.htm",
    "https://www.livesinabox.com/friends/season7/714tat30.htm",
    "https://www.livesinabox.com/friends/season7/715jnb.htm",
    "https://www.livesinabox.com/friends/season7/716tal.htm",
    "https://www.livesinabox.com/friends/season7/717cwd.htm",
    "https://www.livesinabox.com/friends/season7/718towja.htm",
    "https://www.livesinabox.com/friends/season7/719rmac.htm",
    "https://www.livesinabox.com/friends/season7/720rbk.htm",
    "https://www.livesinabox.com/friends/season7/721vows.htm",
    "https://www.livesinabox.com/friends/season7/722towcd.htm",
    "https://www.livesinabox.com/friends/season7/723camw.htm",
    "https://www.livesinabox.com/friends/season7/outtakes.htm"
]

# Loop through Season 7 episodes and fetch content
for title, url in zip(season7_episode_titles, season7_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
