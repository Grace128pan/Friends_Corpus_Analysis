import requests
from bs4 import BeautifulSoup

# Install the required libraries if you haven't already
# You can install them using: pip install requests beautifulsoup4

url = "https://www.livesinabox.com/friends/season1/101pilot.htm"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text content
    page_content = soup.get_text()

    # Specify the file path on your desktop
    file_path = "C:/Users/Grace/Desktop/Episode_101_The_Pilot_Uncut_Version.txt"

    # Write content to a text file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_content)

    print(f"Content has been saved to {file_path}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")


















