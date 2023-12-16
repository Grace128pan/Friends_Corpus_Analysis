import os
import requests
from bs4 import BeautifulSoup

# URL of the page containing the script
url = "https://subslikescript.com/series/Friends-108778/season-4/episode-11-The_One_with_Phoebes_Uterus"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing the script
    script_element = soup.find('div', class_='full-script')

    # Extract the text content of the script
    script_text = script_element.get_text(separator='\n')

    # Define the folder and file names
    folder_name = "FriendsScripts4"
    file_name = "11.season4 The_One_with_Phoebes_Uterus.txt"

    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    # Define the full file path
    file_path = os.path.join(folder_name, file_name)

    # Write the script to a text file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(script_text)

    print(f"Script has been successfully scraped and saved to: {file_path}")

else:
    print(f"Failed to retrieve the content. Status code: {response.status_code}")


