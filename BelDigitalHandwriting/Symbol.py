from . import constants
from .Models.SymbolModels import SymbolRate, VowelConsonantRate
import re


def get_symbol_rate(text: str):
    all_symbol_rate = get_all_symbol_rate(text)
    vowel_consonant_rate = get_vowel_consonant_rate(all_symbol_rate, text)

    symbol_rate = SymbolRate(
        all_symbol_rate,
        vowel_consonant_rate,
        len(text)
    )

    return symbol_rate


def get_vowel_consonant_rate(all_symbol_rate: dict, text: str):
    text = re.sub(r"[^{0}]".format(constants.bel_letters), "", text)

    vowel_count = 0
    consonant_count = 0

    for symbol in list(all_symbol_rate.keys()):
        if symbol in constants.consonant_letters:
            consonant_count += all_symbol_rate[symbol] * len(text)
        elif symbol in constants.vowel_letters:
            vowel_count += all_symbol_rate[symbol] * len(text)

    vowel_consonant_rate = VowelConsonantRate(
        vowel_count / len(text),
        consonant_count / len(text),
        len(text)
    )

    return vowel_consonant_rate


def get_all_symbol_rate(text: str):
    symbol_rates = {}
    for char in text:
        if char not in symbol_rates.keys():
            symbol_rates[char] = 1
        else:
            symbol_rates[char] += 1

    for char, char_count in symbol_rates.items():
        char_rate = char_count / len(text)
        symbol_rates[char] = char_rate

    return symbol_rates
