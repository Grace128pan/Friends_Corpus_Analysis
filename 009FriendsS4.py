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


# Define Season 4 episode titles and corresponding URLs
season4_episode_titles = [
    "Episode 401: The One With The Jellyfish",
    "Episode 402: The One With The Cat",
    "Episode 403: The One With The 'Cuffs",
    "Episode 404: The One With The Ballroom Dancing",
    "Episode 405: The One With Joey's New Girlfriend",
    "Episode 406: The One With The Dirty Girl",
    "Episode 407: The One Where Chandler Crosses the Line",
    "Episode 408: The One With Chandler In A Box",
    "Episode 409: The One Where They're Gonna PARTY!",
    "Episode 410: The One With The Girl From Poughkeepsie",
    "Episode 411: The One With Phoebe's Uterus",
    "Episode 412: The One With The Embryos",
    "Episode 413: The One With Rachel's Crush",
    "Episode 414: The One With Joey's Dirty Day",
    "Episode 415: The One With All The Rugby",
    "Episode 416: The One With The Fake Party",
    "Episode 417: The One With The Free Porn",
    "Episode 418: The One With Rachel's New Dress",
    "Episode 419: The One With All The Haste",
    "Episode 420: The One With All The Wedding Dresses",
    "Episode 421: The One With The Invitation",
    "Episode 422: The One With The Worst Best Man Ever",
    "Episode 423: The One With Ross's Wedding Parts I and II",
    "Episode 423: The One With Ross's Wedding - The Uncut Version"
]

season4_episode_urls = [
    "https://www.livesinabox.com/friends/season4/401jelly.htm",
    "https://www.livesinabox.com/friends/season4/402cat.htm",
    "https://www.livesinabox.com/friends/season4/403cuffs.htm",
    "https://www.livesinabox.com/friends/season4/404dance.htm",
    "https://www.livesinabox.com/friends/season4/405jng.htm",
    "https://www.livesinabox.com/friends/season4/406dirty.htm",
    "https://www.livesinabox.com/friends/season4/407line.htm",
    "https://www.livesinabox.com/friends/season4/408box.htm",
    "https://www.livesinabox.com/friends/season4/409party.htm",
    "https://www.livesinabox.com/friends/season4/410girl.htm",
    "https://www.livesinabox.com/friends/season4/411towpu.htm",
    "https://www.livesinabox.com/friends/season4/412towte.htm",
    "https://www.livesinabox.com/friends/season4/413towrc.htm",
    "https://www.livesinabox.com/friends/season4/414jdd.htm",
    "https://www.livesinabox.com/friends/season4/415rugby.htm",
    "https://www.livesinabox.com/friends/season4/416party.htm",
    "https://www.livesinabox.com/friends/season4/417porn.htm",
    "https://www.livesinabox.com/friends/season4/418dress.htm",
    "https://www.livesinabox.com/friends/season4/419haste.htm",
    "https://www.livesinabox.com/friends/season4/420towwd.htm",
    "https://www.livesinabox.com/friends/season4/421invit.htm",
    "https://www.livesinabox.com/friends/season4/422wbme.htm",
    "https://www.livesinabox.com/friends/season4/423rowed.htm",
    "https://www.livesinabox.com/friends/season4/423uncut.htm"
]

# Loop through Season 4 episodes and fetch content
for title, url in zip(season4_episode_titles, season4_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
