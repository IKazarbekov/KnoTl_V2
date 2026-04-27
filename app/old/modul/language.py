"""
modul for work with learning and translate on three languages:
    English
    Russian
    Bashkir

dependence: not
"""
import requests

def translate_from_api(word: str, from_lang: str, to_lang: str) -> str:
    """
    Translate word to other language, by means api
    :param word:        user word for translate to other language
    :param from_lang:   user word in this language, format: two characters, example en, ru
    :param to_lang:     translate to this language, format: two characters, example en, ru
    :return:            translate word

    :except ConnectionError: if not connection to api for translation
    :example: russian_word = translate_from_api("Hello", "en", "ru")
    """
    if not len(from_lang)== 2:
        raise ValueError(f"Format from_lant:{from_lang} is not great")
    if not len(to_lang) == 2:
        raise ValueError(f"Format to_lang:{to_lang} is not great")
    attempt = 0
    translate = None
    while attempt < 3:
        try:
            translate = requests.get("https://api.mymemory.translated.net/get",
                             params={"q": word, "langpair": from_lang + '|' + to_lang},
                                     timeout=5)
            return translate.json()["responseData"]["translatedText"]
        except Exception:
            attempt += 1
    raise ConnectionError("Error connection to api")

def get_words_from_txt(word: str) -> tuple[str, str]:
    """
    find translation in text file data/language_words.txt
    :param word: word for search, any language
    :return: 2 word other language
    :raise:
        IndexError: If word is not found in file
    :example:
        > get_words("я")
        (""Английский: я", "Башкирский: Мин")
    """
    with open("data/language_words.txt", "r") as file:
        for line in file:
            words = line.strip().split(";")
            if words[0] == word:
                return ("Русский: " + words[1], "Башкирский: " + words[2])
            if words[1] == word:
                return ("Английский: " + words[0], "Башкирский: " + words[2])
            if words[2] == word:
                return ("Английский: " + words[0], "Русский: " + words[1])
    raise IndexError("word not found in dictionary for translate.")

