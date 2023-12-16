import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season4_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season4_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T095941Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3872e9a636790295bee790e42a0b84b2e5f7d9317cbbc6cf41ec19c4c5d87a5fc6a9b3b34e9ee6a5fd33193eef69b2b2ec18b03347c1166ae66a3083af4ec3f5b59608c0198ee0e9a4c65a2deb18e90f4f79ce44ad0cc028e5449b8eb355ac9896b4f952c668599544a9be8c9144e9156434b4fda45d48136ab67d0df70269293e254237d0fda4c3cb1921041f97e68da29c19c469a45a9b9553c47cb48ecc2ed55f23e1f2aae6143af51e58b9d9ecdfd2d79f0ed0c0f35bcf730df4d12c819562d4fb8317561ccb478c5335fd9b229d9dd16dfc161f80295c1b095e1ce90827050c51dd3a26f0e373afb08c9cc7541aa313f925396d4a5643e9e245eb850336"

response = requests.get(season4_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season4_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
