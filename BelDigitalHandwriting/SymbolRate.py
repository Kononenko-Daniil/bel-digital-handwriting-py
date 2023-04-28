from . import constants
import re


def get_symbol_rate(text: str):
    all_symbol_rate = get_all_symbol_rate(text)
    vowel_consonant_rate = get_vowel_consonant_rate(all_symbol_rate, text)

    symbol_rate_info = {
        "symbol_rate": all_symbol_rate,
        "unique_symbols": list(all_symbol_rate.keys()),
        "vowel_consonant_rate": vowel_consonant_rate
    }

    return symbol_rate_info


def get_vowel_consonant_rate(all_symbol_rate: dict, text: str):
    # Застаўляем у тэксце толькі беларускія літары
    text = re.sub(r"[^{0}]".format(constants.bel_letters), "", text)

    vowel_count = 0
    consonant_count = 0

    for symbol in list(all_symbol_rate.keys()):
        if symbol in constants.consonant_letters:
            consonant_count += all_symbol_rate[symbol][0]
        elif symbol in constants.vowel_letters:
            vowel_count += all_symbol_rate[symbol][0]

    vowel_consonant_rate = {
        "vowels": [vowel_count, vowel_count / len(text)],
        "consonant": [consonant_count, consonant_count / len(text)]
    }

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
        symbol_rates[char] = [char_count, char_rate]

    return symbol_rates
