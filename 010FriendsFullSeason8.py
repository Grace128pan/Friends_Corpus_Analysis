import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season8_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season8_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T094852Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3ea58afc23d9f28e11532c6fce3d725bff251003536c3e76347aca2d138fa08e16b724068904678e0b047c77e0fe98282506ef6ebb3f9c593e0197bbc6519416e42470a422c92562c7615df664f80d07efdee1eb1317f574e0c27ae65c26ede539955b57c24912a6141a8cf8b6724284f5ee5c541f9cf157a4a037105b26737f16afff94907b38595e5593d606204570d26277bb7ad217f4e20168dd5e6fb253f57fb727e990d7759f9940553dadaee16ed10c5f7250c38e7eb7221f878a265ff8b879f8d88b003bf15989ba757be7c44c9b5c30c3e52ca74a53c1e18b2620ffe1821cc20801f78e74e3c62b3fa44d5200c95c743a771c14dc4df5c1d3337181"

response = requests.get(season8_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season8_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
