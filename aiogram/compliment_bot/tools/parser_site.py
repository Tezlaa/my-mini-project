import random

from bs4 import BeautifulSoup

import requests


def get_compmliment() -> str:
    url = "https://www.happier.com/blog/nice-things-to-say-100-compliments/"
    response = requests.get(url).text
    
    soup = BeautifulSoup(response, "html.parser")
    
    block = soup.find('ol')
    all_comp = block.find_all('li')
    
    return all_comp[random.randint(0, len(all_comp))].text


if __name__ == "__main__":
    print(get_compmliment())
    