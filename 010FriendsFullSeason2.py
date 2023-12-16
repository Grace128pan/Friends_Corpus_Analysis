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

# URL for Season 2
season2_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season2_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T092626Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=42b6cd298cd1ab2a3dd4c49d4e616abe7a9bdffcf5d0145e2297c7723d1474243f728f01527567220388db5f784e58053d107d7f24b652bd1d800d8173b045a6762a384eb7954011df969ce8e98af9574c7f5cd4bf53ac2e5910acec772fa6a28b4af6cd7cd6442e15b267a14802b4adee5627e99d6f7e96b78ec39928b700a071483d74ad63adf9e1e9e0a45b79fd5578cc477f8427aa72b838a2cc851bfaddf2426697fbdd3af371de76c06fe9556e56bf76c112f5fa4ef8748b44312dd3654b8ca5605027c3fb431327764e00cb17a7ab5095ffd821dc659da582b83f1b41e06c33151df103428642647d5a4730d6e55b8bcd9b46e2ee2b17d4171b8db74f"

# Save Season 2 content
get_and_save_content(season2_url, "season2_friends.txt")

