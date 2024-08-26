import requests


def check_spelling(text: str):
    response = requests.get(
        "https://speller.yandex.net/services/spellservice.json/checkText",
        params={"text": text},
    )
    return response.json()
