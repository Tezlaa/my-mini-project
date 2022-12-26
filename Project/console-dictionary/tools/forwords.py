import requests
from bs4 import BeautifulSoup

def get_transcript(word: str) -> str:
    """
    Args:
        word (str): Your word

    Returns:
        str: transcript your word
    """
    
    data = {
        'text_to_transcribe': 'Hello'
    }

    response = requests.post('https://tophonetics.com/ru/', data=data).text
    soup = BeautifulSoup(response, 'html.parser')
    
    result = soup.find("div", id="transcr_output").text
     
    return result
    
if __name__ == "__main__":
    print(get_transcript("hello"))