import re
from . import constants


def get_word_sentence_rate(text: str):
    word_sentence_rate = {
        "words_rate": get_words_rate(text),
        "sentence_rate": get_sentence_rate(text)
    }

    return word_sentence_rate


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


def get_sentence_rate(text: str):
    sentences = divide_text_to_sentences(text, r"[^{0} \-.?!]".format(constants.bel_letters))
    sentences_comma_included = divide_text_to_sentences(text, r"[^{0} \-,;.?!]".format(constants.bel_letters))

    total_char_len = 0
    for sentence in sentences:
        total_char_len += len(sentence)

    total_words_count = 0
    for sentence in sentences:
        sentence_words = divide_text_to_words(sentence)
        total_words_count += len(sentence_words)

    total_comma_count = 0
    max_comma_count = 0
    for sentence in sentences_comma_included:
        comma_count = len(re.findall(r"[,;]", sentence))
        total_comma_count += comma_count
        if comma_count > max_comma_count:
            max_comma_count = comma_count

    total_exclamation_count = text.count("!")
    total_interrogative_count = text.count("?")

    sentence_count = len(sentences)

    sentence_rate = {
        "sentence_char_len_average": total_char_len / sentence_count,
        "sentence_word_count_average": total_words_count / sentence_count,
        "sentence_count": sentence_count,
        "additional": {
            "comma_average_per_sentence": total_comma_count / sentence_count,
            "max_comma_count": max_comma_count,
            "exclamation_sentence_average": total_exclamation_count / sentence_count,
            "interrogative_sentence_average": total_interrogative_count / sentence_count
        }
    }

    return sentence_rate


def get_words_rate(text: str):
    words = divide_text_to_words(text)
    all_words_len = 0
    for word in words:
        all_words_len += len(word)
    word_len_average = all_words_len / len(words)

    words_rate = {
        "word_len_average": word_len_average,
        "word_count": len(words)
    }

    return words_rate


