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


# Define Season 6 episode titles and corresponding URLs
season6_episode_titles = [
    "Episode 601: The One After Vegas",
    "Episode 602: The One Where Ross Hugs Rachel",
    "Episode 603: The One With Ross's Denial",
    "Episode 604: The One Where Joey Loses His Insurance",
    "Episode 605: The One With Joey's Porsche",
    "Episode 606: The One The Last Night",
    "Episode 607: The One Where Phoebe Runs",
    "Episode 608: The One With Ross's Teeth",
    "Episode 609: The One Where Ross Got High",
    "Episode 610: The One With The Routine",
    "Episode 611: The One With The Apothecary Table",
    "Episode 612: The One With The Joke",
    "Episode 613: The One With Rachel's Sister",
    "Episode 614: The One Where Chandler Can't Cry",
    "Episode 615: The One That Could Have Been",
    "Episode 617: The One With The Unagi",
    "Episode 618: The One Where Ross Dates A Student",
    "Episode 619: The One With Joey's Fridge",
    "Episode 620: The One With Mac And C.H.E.E.S.E.",
    "Episode 621: The One Where Ross Meets Elizabeth's Dad",
    "Episode 622: The One Where Paul's The Man",
    "Episode 623: The One With The Ring",
    "Episode 624: The One With The Proposal"
]

season6_episode_urls = [
    "https://www.livesinabox.com/friends/season6/601vegas.htm",
    "https://www.livesinabox.com/friends/season6/602rhr.htm",
    "https://www.livesinabox.com/friends/season6/603towrd.htm",
    "https://www.livesinabox.com/friends/season6/604jlhi.htm",
    "https://www.livesinabox.com/friends/season6/605towjp.htm",
    "https://www.livesinabox.com/friends/season6/606totln.htm",
    "https://www.livesinabox.com/friends/season6/607towpr.htm",
    "https://www.livesinabox.com/friends/season6/608towrt.htm",
    "https://www.livesinabox.com/friends/season6/609rgh.htm",
    "https://www.livesinabox.com/friends/season6/610towtr.htm",
    "https://www.livesinabox.com/friends/season6/611towat.htm",
    "https://www.livesinabox.com/friends/season6/612joke.htm",
    "https://www.livesinabox.com/friends/season6/613towrs.htm",
    "https://www.livesinabox.com/friends/season6/614ccc.htm",
    "https://www.livesinabox.com/friends/season6/615maybe.htm",
    "https://www.livesinabox.com/friends/season6/617towtu.htm",
    "https://www.livesinabox.com/friends/season6/618rds.htm",
    "https://www.livesinabox.com/friends/season6/619towjf.htm",
    "https://www.livesinabox.com/friends/season6/620mac.htm",
    "https://www.livesinabox.com/friends/season6/621rmed.htm",
    "https://www.livesinabox.com/friends/season6/622pdm.htm",
    "https://www.livesinabox.com/friends/season6/623ring.htm",
    "https://www.livesinabox.com/friends/season6/624towtp.htm"
]

# Loop through Season 6 episodes and fetch content
for title, url in zip(season6_episode_titles, season6_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
