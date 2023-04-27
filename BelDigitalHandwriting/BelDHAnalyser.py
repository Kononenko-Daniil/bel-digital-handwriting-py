import re

from . import SymbolRate
from . import WordSentenceRate
from . import constants


def analyse_text(text: str):
    text = clean_text(text)

    text_info = {
        "text_len": len(text),
        "symbol_rate": SymbolRate.get_symbol_rate(text),
        "word_sentence_rate": WordSentenceRate.get_word_sentence_rate(text)
    }

    return text_info


def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^{0}]".format(constants.accepted_symbols), r"", text)

    return text






