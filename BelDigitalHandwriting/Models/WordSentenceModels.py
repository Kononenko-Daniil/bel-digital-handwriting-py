class VowelConsonantPairRate:
    def __init__(self,
                 pair_count: int,
                 pair_start_rate: dict,
                 pair_end_rate: dict):
        self.pair_count = pair_count
        self.pair_start_rate = pair_start_rate
        self.pair_end_rate = pair_end_rate

    def __dict__(self):
        rate_dict = {
            "pair_count": self.pair_count,
            "pair_start_rate": self.pair_start_rate,
            "pair_end_rate": self.pair_end_rate
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == VowelConsonantPairRate:
            def add_pair_rate(first_pair_rate: dict,
                              second_pair_rate: dict,
                              first_pair_count: int,
                              second_pair_count: int):
                new_pair_rate = {}
                for pair_name in first_pair_rate.keys():
                    new_pair_rate[pair_name] = \
                        (first_pair_rate[pair_name] * first_pair_count +
                         second_pair_rate[pair_name] * second_pair_count) / new_pair_count

                return new_pair_rate

            new_pair_count = self.pair_count + other.pair_count
            new_start_pair_rate = add_pair_rate(self.pair_start_rate,
                                                other.pair_start_rate,
                                                self.pair_count,
                                                other.pair_count)
            new_end_pair_rate = add_pair_rate(self.pair_end_rate,
                                              other.pair_end_rate,
                                              self.pair_count,
                                              other.pair_count)

            new_rate = VowelConsonantPairRate(
                new_pair_count,
                new_start_pair_rate,
                new_end_pair_rate
            )

            return new_rate

        return None


class SpeechPartRate:
    def __init__(self,
                 speech_part_rate: dict,
                 recognized_words_count: int):
        self.speech_part_rate = speech_part_rate
        self.recognized_words_count = recognized_words_count

    def __dict__(self):
        rate_dict = {
            "speech_part_rate": self.speech_part_rate,
            "recognized_words_count": self.recognized_words_count
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == SpeechPartRate:
            new_recognized_words_count = self.recognized_words_count + other.recognized_words_count
            new_speech_part_rate = {}

            for speech_part in self.speech_part_rate.keys():
                self_speech_part_count = self.speech_part_rate[speech_part] * self.recognized_words_count
                other_speech_part_count = other.speech_part_rate[speech_part] * other.recognized_words_count

                speech_part_count = self_speech_part_count + other_speech_part_count
                new_speech_part_rate[speech_part] = speech_part_count / new_recognized_words_count

            new_rate = SpeechPartRate(
                new_speech_part_rate,
                new_recognized_words_count
            )

            return new_rate

        return None


class WordRate:
    def __init__(self,
                 word_count: int,
                 word_len_average: float,
                 speech_part_rate: SpeechPartRate,
                 vowel_consonant_pair_rate: VowelConsonantPairRate):
        self.word_count = word_count
        self.word_len_average = word_len_average
        self.speech_part_rate = speech_part_rate
        self.vowel_consonant_pair_rate = vowel_consonant_pair_rate

    def __dict__(self):
        rate_dict = {
            "word_count": self.word_count,
            "word_len_average": self.word_len_average,
            "speech_part_rate": self.speech_part_rate.__dict__(),
            "vowel_consonant_pair_rate": self.vowel_consonant_pair_rate.__dict__()
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == WordRate:
            new_word_count = self.word_count + other.word_count
            new_word_len_average = \
                (self.word_len_average * self.word_count +
                 other.word_len_average * other.word_count) / new_word_count
            new_speech_part_rate = self.speech_part_rate + other.speech_part_rate
            new_vowel_consonant_pair_rate = self.vowel_consonant_pair_rate + other.vowel_consonant_pair_rate

            new_rate = WordRate(
                new_word_count,
                new_word_len_average,
                new_speech_part_rate,
                new_vowel_consonant_pair_rate
            )

            return new_rate

        return None


class SentenceRate:
    def __init__(self,
                 sentence_count: int,
                 sentence_char_len_average: float,
                 sentence_word_count_average: float,
                 comma_average_per_sentence: float,
                 max_comma_count: int,
                 exclamation_sentence_average: float,
                 interrogative_sentence_average: float):
        self.sentence_count = sentence_count
        self.sentence_char_len_average = sentence_char_len_average
        self.sentence_word_count_average = sentence_word_count_average
        self.comma_average_per_sentence = comma_average_per_sentence
        self.max_comma_count = max_comma_count
        self.exclamation_sentence_average = exclamation_sentence_average
        self.interrogative_sentence_average = interrogative_sentence_average

    def __dict__(self):
        rate_dict = {
            "sentence_count": self.sentence_count,
            "sentence_char_len_average": self.sentence_char_len_average,
            "sentence_word_count_average": self.sentence_word_count_average,
            "comma_average_per_sentence": self.comma_average_per_sentence,
            "max_comma_count": self.max_comma_count,
            "exclamation_sentence_average": self.exclamation_sentence_average,
            "interrogative_sentence_average": self.interrogative_sentence_average,
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == SentenceRate:
            def get_new_average(self_value, other_value):
                new_value = \
                    (self_value * self.sentence_count +
                     other_value * other.sentence_count) / new_sentence_count

                return new_value

            new_sentence_count = self.sentence_count + other.sentence_count
            new_sentence_char_len_average = get_new_average(self.sentence_char_len_average,
                                                            other.sentence_char_len_average)
            new_sentence_word_count_average = get_new_average(self.sentence_word_count_average,
                                                              other.sentence_word_count_average)
            new_comma_average_per_sentence = get_new_average(self.comma_average_per_sentence,
                                                             other.comma_average_per_sentence)
            new_max_comma_count = max(self.max_comma_count, other.max_comma_count)
            new_exclamation_sentence_average = get_new_average(self.exclamation_sentence_average,
                                                               other.exclamation_sentence_average)
            new_interrogative_sentence_average = get_new_average(self.interrogative_sentence_average,
                                                                 other.interrogative_sentence_average)

            new_rate = SentenceRate(
                new_sentence_count,
                new_sentence_char_len_average,
                new_sentence_word_count_average,
                new_comma_average_per_sentence,
                new_max_comma_count,
                new_exclamation_sentence_average,
                new_interrogative_sentence_average
            )

            return new_rate

        return None


class WordSentenceRate:
    def __init__(self,
                 word_rate: WordRate,
                 sentence_rate: SentenceRate):
        self.word_rate = word_rate
        self.sentence_rate = sentence_rate

    def __dict__(self):
        rate_dict = {
            "word_rate": self.word_rate.__dict__(),
            "sentence_rate": self.sentence_rate.__dict__()
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == WordSentenceRate:
            new_rate = WordSentenceRate(
                self.word_rate + other.word_rate,
                self.sentence_rate + other.sentence_rate
            )

            return new_rate

        return None


def vowel_consonant_pair_rate_from_dict(rate_dict: dict) -> VowelConsonantPairRate:
    vowel_consonant_pair_rate = VowelConsonantPairRate(
        rate_dict["pair_count"],
        rate_dict["pair_start_rate"],
        rate_dict["pair_end_rate"]
    )

    return vowel_consonant_pair_rate


def speech_part_rate_from_dict(rate_dict: dict) -> SpeechPartRate:
    speech_part_rate = SpeechPartRate(
        rate_dict["speech_part_rate"],
        rate_dict["recognized_words_count"]
    )

    return speech_part_rate


def word_rate_from_dict(rate_dict: dict) -> WordRate:
    word_rate = WordRate(
        rate_dict["word_count"],
        rate_dict["word_len_average"],
        speech_part_rate_from_dict(
            rate_dict["speech_part_rate"]
        ),
        vowel_consonant_pair_rate_from_dict(
            rate_dict["vowel_consonant_pair_rate"]
        )
    )

    return word_rate


def sentence_rate_from_dict(rate_dict: dict) -> SentenceRate:
    sentence_rate = SentenceRate(
        rate_dict["sentence_count"],
        rate_dict["sentence_char_len_average"],
        rate_dict["sentence_word_count_average"],
        rate_dict["comma_average_per_sentence"],
        rate_dict["max_comma_count"],
        rate_dict["exclamation_sentence_average"],
        rate_dict["interrogative_sentence_average"]
    )

    return sentence_rate


def word_sentence_rate_from_dict(rate_dict: dict) -> WordSentenceRate:
    word_sentence_rate = WordSentenceRate(
        word_rate_from_dict(rate_dict["word_rate"]),
        sentence_rate_from_dict(rate_dict["sentence_rate"])
    )

    return word_sentence_rate
