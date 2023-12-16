import os
import requests
from bs4 import BeautifulSoup

# Function to get content and save to file
def get_and_save_content(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text content
        page_content = soup.get_text()

        # Specify the file path on your desktop inside the 'Full' folder
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_path = os.path.join(desktop_path, "Full")
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)

        # Write content to a text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(page_content)

        print(f"Content has been saved to {file_path}")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

# URL for Season 1
season1_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season1_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T092220Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=555d9f0ebf7b0aeb192981c734c3e55efd8b9625986e11aaf2cab9ef1ebcf910b6bf8fb65f4aea28c5aa7fbc9a1fde477723f120dd0ce8a0ae24e78b1f73e778b34b46c138fa8906a9e2e1b367a81153db276fcb791232aa900cf462ef1979a5fc558ec0126d15c1df08113a13a0512568180bade0382634877096dbd4d750e8e855e5ca946dcfd4edb6efa404cd7917da42c899316f823b40b0040fcef72824f3ef64b5d05aebf4cad59148fd2228f6cd048e4e31b703915d57a5c32b0385f39389d34d8328a33f6a1b15e07e94f2d07877c20ba71ce655dfe1f552633c068622ed74abc1f944af529e6b650bea94a4e82ce68d05493e90360f3d845bd563de"

# Save Season 1 content
get_and_save_content(season1_url, "season1_friends.txt")



