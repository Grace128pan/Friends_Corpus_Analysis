import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season5_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season5_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T095758Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=7924fb775f3ea0d9d88e63ddb51a1081543eb49ab55bfec44a205fcf43aeca099eac4a0fe5f14bf43e80b43c780ac8fbe0e61e51c367d5d0ef008088c5952b3edfd9feba94eb7063e576b321190acff2cde226f9a3a886130c33c989112ec520c4216b360849ae1d42a6628f97f7d7f70ac92eb5a3fd011fa9a4e460721cf23d3046a35921cf2fc09149de8cb4268eefdcced5295321e4e29c661a5bb0ee8a94c4376b55cbe2fa3815aa4d961c619b1432875c48c6b8b725f903b0947c0ce4a7a4ad7ed2907db766ab7a35bb3d183bfc464208622beb6ceac56143c128b199b9022e55dbc41aa90c66aaaf29d24ed624339033aef3a16871a959947d526cfcd0"

response = requests.get(season5_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season5_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
