import re
import os
import pkg_resources
from . import constants
from .Models.WordSentenceModels import *


def get_word_sentence_rate(text: str):
    word_sentence_rate = WordSentenceRate(
        get_words_rate(text),
        get_sentence_rate(text)
    )

    return word_sentence_rate


def get_words_rate(text: str):
    word_len_average, word_count = get_word_len_rate(text)
    speech_part_rate = get_speech_part_word_rate(text)
    vowel_consonant_pair_rate = get_vowel_consonant_pair_rate(text)

    words_rate = WordRate(
        word_count,
        word_len_average,
        speech_part_rate,
        vowel_consonant_pair_rate
    )

    return words_rate


def get_sentence_rate(text: str):
    sentences = divide_text_to_sentences(text, r"[^{0} \-.?!]".format(constants.bel_letters))
    sentences_punctuation_included = divide_text_to_sentences(
        text,
        r"[^{0} \-,;.?!]".format(constants.bel_letters)
    )

    sentence_count = len(sentences)

    sentence_char_len_average = get_sentence_char_len_average(sentences)
    sentence_word_count_average = get_sentence_word_len_average(sentences)
    comma_average_per_sentence, max_comma_count = get_sentence_comma_rate(sentences_punctuation_included)
    exclamation_sentence_average = get_symbol_per_sentence_rate(text, sentence_count, "!")
    interrogative_sentence_average = get_symbol_per_sentence_rate(text, sentence_count, "?")

    sentence_rate = SentenceRate(
        sentence_count,
        sentence_char_len_average,
        sentence_word_count_average,
        comma_average_per_sentence,
        max_comma_count,
        exclamation_sentence_average,
        interrogative_sentence_average,
    )

    return sentence_rate


def delete_unnecessary_spaces(text: str):
    while text.find("  ") != -1:
        text = re.sub(r"  ", " ", text)

    return text


def divide_text_to_words(text: str):
    text = re.sub(r"[^{0} -]".format(constants.bel_letters), "", text)
    text = re.sub(r" - ", " ", text)
    text = delete_unnecessary_spaces(text)

    words = text.split(" ")

    return words


def divide_text_to_sentences(text: str, stayed_symbols: str):
    text = re.sub(stayed_symbols, "", text)
    text = re.sub(r" - ", " ", text)
    text = delete_unnecessary_spaces(text)

    sentences = re.split(r"[.!?]", text)
    full_sentences = []
    for sentence in sentences:
        if sentence != "":
            cleaned_sentence = sentence
            if sentence[0] == " ":
                cleaned_sentence = sentence[1:]
            full_sentences.append(cleaned_sentence)
    sentences = full_sentences

    return sentences


def get_sentence_char_len_average(sentences: list):
    total_char_len = 0
    for sentence in sentences:
        total_char_len += len(sentence)

    sentence_count = len(sentences)
    average = total_char_len / sentence_count
    return average


def get_sentence_word_len_average(sentences: list):
    total_words_count = 0
    for sentence in sentences:
        sentence_words = divide_text_to_words(sentence)
        total_words_count += len(sentence_words)

    sentence_count = len(sentences)
    average = total_words_count / sentence_count

    return average


def get_sentence_comma_rate(sentences: list):
    total_comma_count = 0
    max_comma_count = 0
    for sentence in sentences:
        comma_count = len(re.findall(r"[,;]", sentence))
        total_comma_count += comma_count
        if comma_count > max_comma_count:
            max_comma_count = comma_count

    sentence_count = len(sentences)
    average = total_comma_count / sentence_count

    return average, max_comma_count


def get_symbol_per_sentence_rate(text: str, sentence_count: int, symbol):
    total_symbol_count = text.count(symbol)
    average = total_symbol_count / sentence_count

    return average


def get_vowel_consonant_pair_rate(text: str):
    words = divide_text_to_words(text)
    word_pairs = []
    pair_start_rate = {"VV": 0, "CV": 0, "VC": 0, "CC": 0}
    pair_end_rate = {"VV": 0, "CV": 0, "VC": 0, "CC": 0}

    for i in range(0, len(words) - 1):
        def get_word_letter_type(word: str, is_first: bool):
            if is_first:
                index = 0
            else:
                index = len(word)-1
            if word[index] in constants.vowel_letters:
                return "V"
            else:
                return "C"

        res_pair_start = get_word_letter_type(words[i], True) + get_word_letter_type(words[i+1], True)
        res_pair_end = get_word_letter_type(words[i], False) + get_word_letter_type(words[i+1], False)
        word_pairs.append([res_pair_start, res_pair_end])

    for pair in constants.pair_types:
        for word_pair in word_pairs:
            if word_pair[0] == pair:
                pair_start_rate[pair] += 1
            if word_pair[1] == pair:
                pair_end_rate[pair] += 1
        pair_start_rate[pair] /= len(word_pairs)
        pair_end_rate[pair] /= len(word_pairs)

    vowel_consonant_pair_rate = VowelConsonantPairRate(
        len(word_pairs),
        pair_start_rate,
        pair_end_rate
    )

    return vowel_consonant_pair_rate


def get_speech_part_word_rate(text: str):
    words = divide_text_to_words(text)
    slouniki_dir = pkg_resources.resource_filename('BelDigitalHandwriting', 'slouniki_parsed/')
    speech_part_rate = {}

    recognized_words_count = 0
    for slounik_name in os.listdir(slouniki_dir):
        slounik_path = os.path.join(slouniki_dir, slounik_name)
        slounik = open(slounik_path, 'r', encoding='utf-8')
        slounik_data = slounik.read().split('#')
        for word in words:
            if word in slounik_data:
                recognized_words_count += 1
                speech_part_gr = constants.speech_parts_gr[slounik_name]
                word += "+"
                if speech_part_gr in speech_part_rate.keys():
                    speech_part_rate[speech_part_gr] += 1
                else:
                    speech_part_rate[speech_part_gr] = 1

    for speech_part in speech_part_rate.keys():
        speech_part_rate[speech_part] /= recognized_words_count

    speech_part_rate = SpeechPartRate(
        speech_part_rate,
        recognized_words_count
    )

    return speech_part_rate


def get_word_len_rate(text: str):
    words = divide_text_to_words(text)
    all_words_len = 0
    for word in words:
        all_words_len += len(word)
    word_len_average = all_words_len / len(words)

    return word_len_average, len(words)





