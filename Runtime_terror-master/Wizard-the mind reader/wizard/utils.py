

from .exceptions import InvalidAnswerError, InvalidLanguageError, AkiConnectionFailure, AkiTimedOut, AkiNoQuestions, AkiServerDown, AkiTechnicalError


def ans_to_id(ans):
   

    ans = str(ans).lower()
    if ans == "yes" or ans == "y" or ans == "0":
        return "0"
    elif ans == "no" or ans == "n" or ans == "1":
        return "1"
    elif ans == "i" or ans == "idk" or ans == "i dont know" or ans == "i don't know" or ans == "2":
        return "2"
    elif ans == "probably" or ans == "p" or ans == "3":
        return "3"
    elif ans == "probably not" or ans == "pn" or ans == "4":
        return "4"
    else:
        raise InvalidAnswerError("""
        You put "{}", which is an invalid answer.
        The answer must be one of these:
            - "yes" OR "y" OR "0" for YES
            - "no" OR "n" OR "1" for NO
            - "i" OR "idk" OR "i dont know" OR "i don't know" OR "2" for I DON'T KNOW
            - "probably" OR "p" OR "3" for PROBABLY
            - "probably not" OR "pn" OR "4" for PROBABLY NOT
        """.format(ans))


def get_region(lang=None):

    if lang:
        lang = lang.lower().replace(" ", "")
        if lang.endswith(("animal", "object")):
            lang += "s"

    if lang is None or lang == "en" or lang == "english":
        return "srv14.wizard.com:9281"
    elif lang == "en2" or lang == "english2":
        return "srv6.wizard.com:9126"
    elif lang == "en3" or lang == "english3":
        return "srv11.wizard.com:9152"
    elif lang == "en_animals" or lang == "english_animals":
        return "srv2.wizard.com:9307"
    elif lang == "en_objects" or lang == "english_objects":
        return "srv2.wizard.com:9308"
    elif lang == "ar" or lang == "arabic":
        return "srv2.wizard.com:9304"
    elif lang == "cn" or lang == "chinese":
        return "srv11.wizard.com:9150"
    elif lang == "de" or lang == "german":
        return "srv14.wizard.com:9283"
    elif lang == "de_animals" or lang == "german_animals":
        return "srv14.wizard.com:9284"
    elif lang == "es" or lang == "spanish":
        return "srv6.wizard.com:9127"
    elif lang == "es2" or lang == "spanish2":
        return "srv11.wizard.com:9151"
    elif lang == "es_animals" or lang == "spanish_animals":
        return "srv13.wizard.com:9257"
    elif lang == "fr" or lang == "french":
        return "srv3.wizard.com:9217"
    elif lang == "fr2" or lang == "french2":
        return "srv12.wizard.com:9185"
    elif lang == "fr_animals" or lang == "french_animals":
        return "srv3.wizard.com:9259"
    elif lang == "fr_objects" or lang == "french_objects":
        return "srv3.wizard.com:9218"
    elif lang == "il" or lang == "hebrew":
        return "srv12.wizard.com:9189"
    elif lang == "it" or lang == "italian":
        return "srv9.wizard.com:9214"
    elif lang == "it_animals" or lang == "italian_animals":
        return "srv9.wizard.com:9261"
    elif lang == "jp" or lang == "japanese":
        return "srv11.wizard.com:9172"
    elif lang == "jp_animals" or lang == "japanese_animals":
        return "srv11.wizard.com:9263"
    elif lang == "kr" or lang == "korean":
        return "srv2.wizard.com:9305"
    elif lang == "nl" or lang == "dutch":
        return "srv9.wizard.com:9215"
    elif lang == "pl" or lang == "polish":
        return "srv14.wizard.com:9282"
    elif lang == "pt" or lang == "portuguese":
        return "srv11.wizard.com:9174"
    elif lang == "ru" or lang == "russian":
        return "srv12.wizard.com:9190"
    elif lang == "tr" or lang == "turkish":
        return "srv3.wizard.com:9211"
    else:
        raise InvalidLanguageError("You put \"{}\", which is an invalid language.".format(lang))


def raise_connection_error(response):
    """Raise the proper error if the API failed to connect"""

    if response == "KO - SERVER DOWN":
        raise AkiServerDown("wizard's servers are down in this region. Try again later or use a different language")
    elif response == "KO - TECHNICAL ERROR":
        raise AkiTechnicalError("wizard's servers have had a technical error. Try again later or use a different language")
    elif response == "KO - TIMEOUT":
        raise AkiTimedOut("Your wizard session has timed out")
    elif response == "WARN - NO QUESTION":
        raise AkiNoQuestions("\"wizard.step\" reached 80. No more questions")
    else:
        raise AkiConnectionFailure("An unknown error has occured. Server response: {}".format(response))
