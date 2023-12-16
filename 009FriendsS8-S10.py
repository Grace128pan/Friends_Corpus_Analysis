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


# Define Season 8 episode titles and corresponding URLs
season8_episode_titles = [
    "Episode 801: The One After 'I Do'",
    "Episode 802: The One With The Red Sweater",
    "Episode 803: The One Where Rachel Tells...",
    "Episode 804: The One With The Videotape",
    "Episode 805: The One With Rachel's Date",
    "Episode 806: The One With The Halloween Party",
    "Episode 807: The One With The Stain",
    "Episode 808: The One With The Stripper",
    "Episode 809: The One With The Rumor",
    "Episode 810: The One With Monica's Boots",
    "Episode 811: The One With Ross's Big Step Forward",
    "Episode 812: The One Where Joey Dates Rachel",
    "Episode 813: The One Where Chandler Takes A Bath",
    "Episode 814: The One With The Secret Closet",
    "Episode 815: The One With The Birthing Video",
    "Episode 816: The One Where Joey Tells Rachel",
    "Episode 817: The One With The Tea Leaves",
    "Episode 818: The One In Massapequa",
    "Episode 819: The One With Joey's Interview",
    "Episode 820: The One With The Baby Shower",
    "Episode 821: The One With The Cooking Class",
    "Episode 822: The One Where Rachel Is Late",
    "Episode 823: The One Where Rachel Has A Baby"
]

season8_episode_urls = [
    "https://www.livesinabox.com/friends/season8/801ido.htm",
    "https://www.livesinabox.com/friends/season8/802towrs.htm",
    "https://www.livesinabox.com/friends/season8/803towrt.htm",
    "https://www.livesinabox.com/friends/season8/804towvt.htm",
    "https://www.livesinabox.com/friends/season8/805towrd.htm",
    "https://www.livesinabox.com/friends/season8/806towhp.htm",
    "https://www.livesinabox.com/friends/season8/807stain.htm",
    "https://www.livesinabox.com/friends/season8/808strip.htm",
    "https://www.livesinabox.com/friends/season8/809rumor.htm",
    "https://www.livesinabox.com/friends/season8/810boots.htm",
    "https://www.livesinabox.com/friends/season8/811rbsf.htm",
    "https://www.livesinabox.com/friends/season8/812jdr.htm",
    "https://www.livesinabox.com/friends/season8/813ctab.htm",
    "https://www.livesinabox.com/friends/season8/814towsc.htm",
    "https://www.livesinabox.com/friends/season8/815towbv.htm",
    "https://www.livesinabox.com/friends/season8/816jtr.htm",
    "https://www.livesinabox.com/friends/season8/817towtl.htm",
    "https://www.livesinabox.com/friends/season8/818toim.htm",
    "https://www.livesinabox.com/friends/season8/819towji.htm",
    "https://www.livesinabox.com/friends/season8/820towbs.htm",
    "https://www.livesinabox.com/friends/season8/821towcc.htm",
    "https://www.livesinabox.com/friends/season8/822ril.htm",
    "https://www.livesinabox.com/friends/season8/823rhab.htm"
]

# Loop through Season 8 episodes and fetch content
for title, url in zip(season8_episode_titles, season8_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)

# Define Season 9 episode titles and corresponding URLs
season9_episode_titles = [
    "Episode 901: The One Where No One Proposes",
    "Episode 902: The One Where Emma Cries",
    "Episode 903: The One With The Pediatrician",
    "Episode 904: The One With The Sharks",
    "Episode 905: The One With Phoebe's Birthday Dinner",
    "Episode 906: The One With The Male Nanny",
    "Episode 907: The One With Ross's Inappropriate Song",
    "Episode 908: The One With Rachel's Other Sister",
    "Episode 909: The One With Rachel's Phone Number",
    "Episode 910: The One With Christmas In Tulsa",
    "Episode 911: The One Where Rachel Goes Back To Work",
    "Episode 912: The One With Phoebe's Rats",
    "Episode 913: The One Where Monica Sings",
    "Episode 914: The One With The Blind Dates",
    "Episode 915: The One With The Mugging",
    "Episode 916: The One With The Boob Job",
    "Episode 917: The One With The Memorial Service",
    "Episode 918: The One With The Lottery",
    "Episode 919: The One With Rachel's Dream",
    "Episode 920: The One With The Soap Opera Party",
    "Episode 921: The One With The Fertility Test",
    "Episode 922: The One With The Donor",
    "Episode 923: The One In Barbados (1)",
    "Episode 924: The One In Barbados (2)"
]

season9_episode_urls = [
    "https://www.livesinabox.com/friends/season9/901nop.htm",
    "https://www.livesinabox.com/friends/season9/902towec.htm",
    "https://www.livesinabox.com/friends/season9/903ped.htm",
    "https://www.livesinabox.com/friends/season9/904sharks.htm",
    "https://www.livesinabox.com/friends/season9/905.htm",
    "https://www.livesinabox.com/friends/season9/906nanny.htm",
    "https://www.livesinabox.com/friends/season9/907song.htm",
    "https://www.livesinabox.com/friends/season9/908rachelsister.htm",
    "https://www.livesinabox.com/friends/season9/909rachelnumber.htm",
    "https://www.livesinabox.com/friends/season9/910xmas.htm",
    "https://www.livesinabox.com/friends/season9/911work.htm",
    "https://www.livesinabox.com/friends/season9/912rats.htm",
    "https://www.livesinabox.com/friends/season9/913sings.htm",
    "https://www.livesinabox.com/friends/season9/914dates.htm",
    "https://www.livesinabox.com/friends/season9/915mug.htm",
    "https://www.livesinabox.com/friends/season9/916boob.htm",
    "https://www.livesinabox.com/friends/season9/917service.htm",
    "https://www.livesinabox.com/friends/season9/918lottery.htm",
    "https://www.livesinabox.com/friends/season9/919dream.htm",
    "https://www.livesinabox.com/friends/season9/920party.htm",
    "https://www.livesinabox.com/friends/season9/921test.htm",
    "https://www.livesinabox.com/friends/season9/0922.html",
    "https://www.livesinabox.com/friends/season9/0923-0924.html"
    "https://www.livesinabox.com/friends/season9/0923-0924.html"
]

# Loop through Season 9 episodes and fetch content
for title, url in zip(season9_episode_titles, season9_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)

# Define Season 10 episode titles and corresponding URLs
season10_episode_titles = [
    "Episode 1001: The One After Joey and Rachel Kiss",
    "Episode 1002: The One Where Ross is Fine",
    "Episode 1003: The One With Ross' Tan",
    "Episode 1004: The One With The Cake",
    "Episode 1005: The One Where Rachel's Sister Babysits",
    "Episode 1006: The One With Ross' Grant",
    "Episode 1007: The One With The Home Study",
    "Episode 1008: The One With The Late Thanksgiving",
    "Episode 1009: The One With The Birth Mother",
    "Episode 1010: The One Where Chandler Gets Caught",
    "Episode 1011: The One Where the Stripper Cries",
    "Episode 1012: The One With Phoebe's Wedding",
    "Episode 1013: The One Where Joey Speaks French",
    "Episode 1014: The One With Princess Consuela",
    "Episode 1015: The One Where Estelle Dies",
    "Episode 1016: The One With Rachel's Going Away Party",
    "Episode 1017: The Last One (1)",
    "Episode 1018: The Last One (2)"
]

season10_episode_urls = [
    "https://www.livesinabox.com/friends/1001.shtml",
    "https://www.livesinabox.com/friends/1002.shtml",
    "https://www.livesinabox.com/friends/1003.shtml",
    "https://www.livesinabox.com/friends/1004.shtml",
    "https://www.livesinabox.com/friends/1005.shtml",
    "https://www.livesinabox.com/friends/1006.shtml",
    "https://www.livesinabox.com/friends/1007.shtml",
    "https://www.livesinabox.com/friends/1008.shtml",
    "https://www.livesinabox.com/friends/1009.shtml",
    "https://www.livesinabox.com/friends/1010.shtml",
    "https://www.livesinabox.com/friends/1011.shtml",
    "https://www.livesinabox.com/friends/1012.shtml",
    "https://www.livesinabox.com/friends/1013.shtml",
    "https://www.livesinabox.com/friends/1014.shtml",
    "https://www.livesinabox.com/friends/1015.shtml",
    "https://www.livesinabox.com/friends/1016.shtml",
    "https://www.livesinabox.com/friends/1017.shtml",
    "https://www.livesinabox.com/friends/1018.shtml"
]

# Loop through Season 10 episodes and fetch content
for title, url in zip(season10_episode_titles, season10_episode_urls):
    file_name = f"{title.replace(':', ' -')}.txt"
    get_and_save_content(url, file_name)
