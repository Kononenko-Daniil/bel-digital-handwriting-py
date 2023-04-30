import re

from . import Symbol
from . import WordSentence
from . import constants
from .Models.AnalyzeModels import *


def analyse_text(text: str):
    text = clean_text(text)

    analyze_result = BelDHAnalyze(
        len(text),
        Symbol.get_symbol_rate(text),
        WordSentence.get_word_sentence_rate(text)
    )

    return analyze_result


def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^{0}]".format(constants.accepted_symbols), r"", text)

    return text






