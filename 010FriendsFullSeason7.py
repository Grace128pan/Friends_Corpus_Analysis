import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season7_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season7_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T095310Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=7fbd5d4be2e16b8cf5811ef2d7287687091758253981a64c02fd235e197ba1166ca886a30effd137a9f350795d3454717aaece042806a6e78c26272a7df597ad2f5568357b1df72b5d32a7e29d09905087490bcbc9aa1da4dbc28caf91f48b0391670d92034cacaf63c1f48a98a5465f500171d72ebd61fcbe9d046bdbbb0a763dd04f6a382650b290a97ab6880cb2a7ee85f993f8cbae71c1dd8da9e6865e81eae4c0576b5813ea23b378dc411f67dddca0931442ec41413ee8e836ba2636f48c2d04190aaa7ae309f0b34d4e6c372ea2804c260ccaa972abd047f0b911e535829fb229d11a01e7464dca6c8ef5311d15e65e477adf0cd999d17a02552fc307"

response = requests.get(season7_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season7_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
