from bs4 import BeautifulSoup

import requests


def get_transcript(word: str) -> str:
    """
    Args:
        word (str): Your word

    Returns:
        str: transcript your word
    """
    if word is None:
        return "None"

    data = {
        'text_to_transcribe': word,
    }

    response = requests.post('https://tophonetics.com/ru/', data=data).text
    soup = BeautifulSoup(response, 'html.parser')

    result = soup.find("div", id="transcr_output").text

    return result


def get_translate(word: str) -> str:
    """
    Args:
        word (str): word on english for translate since deepL

    Returns:
        str: result translate
    """


if __name__ == "__main__":
    print(get_transcript("hello"))
