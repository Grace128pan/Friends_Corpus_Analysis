import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season3_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season3_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T100134Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=332f285632f456b52cce5814a222386780b72955b962d3548bae0daf1249f0d930cceb4bbc953362a432d2906b59178db7e6f5a4d68f4521ecf91057c33489c96b8e3144ef1e33ac1934dc5b3d1fef02c036413922fdf3980ea925bd220e3a2720628e5817829d8f09a8080a65bc93b4c864df5bfca68f6060142e26a59efeaa98bb52a956e227f9c573c0264974d1dbd0700cf433d1089b0356286933f371a8f613f0b9a3b21a71d5f729034c800d979841a2e014cb436e7a5954a95fa9ca51eae94f6af00700bac541dabd78c69d6d3b3e63a8db637cedffc967ba40f93fbd89eeefa693e2914b5ed55cde10a83538e8e4a8ab090284d5949c7d0c9b88e695"

response = requests.get(season3_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season3_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
