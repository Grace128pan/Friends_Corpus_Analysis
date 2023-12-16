import requests
from bs4 import BeautifulSoup

# Replace the URL with the correct one if needed
season6_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1627227/2674316/season6_friends.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231207T095603Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=09cb23fb629847ef75e1210f19e0ab20628736ba2d63f254c3453913769784b7082d2272d35696d403c9069b7892c223bf7001fc41d3a537ca2278ef18ac3e6ae38b66d7c66259115c2f21873f4b81bc121205b154bcbf5b7072593b6aea31a3a5c7e4c7c090945eb8cb8404af3f0645a7686b7dd7007767fb0aa9a6ada9b851b9452227a650663dea83a1c29d9113af59d7c14f9045deb2522a0e3373bcfc4e0d7b0171d5f1ac9f2ccc70ff95b13bcd673631c9208f60bf3ae5cfc2522312bb31caf44610634d939b80734822c547fe1015e4d7f90e4eefe532c12e5fb3bebbbbee91c9a24855409e8dde9bf725ea73621af75ec52c4e7de2fb5653eae03cca"

response = requests.get(season6_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Save the content to a file
    with open('season6_friends.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print('Content saved successfully.')
else:
    print(f'Failed to fetch content. Status code: {response.status_code}')
