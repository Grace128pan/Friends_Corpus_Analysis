import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season10_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season10_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T093144Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=069348419c3a66133e6cd620930d97f01aba4e3985f3cfb7eebeb6e6d33e59d6660b2ed96b3b79834684383e1690bc59cbd91719481501fd30663453fda834a7f17faf8778b316e1910b62687bf270ef3c3435ce61f6aaf1dbfdc24761222dadfeed9761e47adf780f976bb736e64dbadcd64a08ee4a664cec857ebb337e509912495909cf9dcaf59ccac5de7200643f20346a8e2ded3a77a92cccba594203da0a2e5b91185eaf22d326947307e52ea58e0051aa91442d203e9b7978ac710b4f7ecb38bf3758bb1db0003bc5a45aa1f3eecc67f634727aa4ec6b6295e36dda9ebacb0341bea3e26f2017acd5e1afbd6d6e5b62d8be12fa2226153c0d5435aa30"

response = requests.get(season10_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season10_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
