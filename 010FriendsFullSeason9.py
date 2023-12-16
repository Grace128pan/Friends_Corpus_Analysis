import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season9_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season9_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T094638Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=76377eafcc818507c4b1e5620cde72fb6a79fac39ab84cefbeeb43f655ff3ed417256c78f345a8c5737b4dc08fe7351b069193b74f65a9d614b009671b317a17482f1cb91ea487ce45830031a73681dc8001a91b7a171ddd4133a33bca065fa74c9e5917bdc92a2c1b00f285f5e06d2364d05559bcf5354d4ee8280dccaa513ef1ee37651efd27a883ceb764974f4b8729335d8fcd18499980cea77a923042aeb581e84648144298f6961a2c625dc37859339d7335c37d73f189a2dfd8a8534d8a662417bb91ffc545a0bf3dbba8ee8aff2528985fa040ce62987130a61ab9fa1e5e78405bfcaea35a2289cd57409f62e5b49d64612923ce6fe332ae4b18af96"

response = requests.get(season9_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season9_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
