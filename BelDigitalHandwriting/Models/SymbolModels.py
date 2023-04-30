class VowelConsonantRate:
    def __init__(self,
                 vowels_rate: float,
                 consonant_rate: float,
                 text_len: int):
        self.vowels_rate = vowels_rate
        self.consonant_rate = consonant_rate
        self.text_len = text_len

    def __dict__(self):
        rate_dict = {
            "vowels_rate": self.vowels_rate,
            "consonant_rate": self.consonant_rate,
            "text_len": self.text_len
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == VowelConsonantRate:
            new_text_len = self.text_len + other.text_len
            new_vowels_count = self.vowels_rate * self.text_len + other.vowels_rate * other.text_len
            new_consonant_count = self.consonant_rate * self.text_len + other.consonant_rate * other.text_len

            new_vowel_rate = new_vowels_count / new_text_len
            new_consonant_rate = new_consonant_count / new_text_len

            new_vowel_consonant_rate = VowelConsonantRate(
                new_vowel_rate,
                new_consonant_rate,
                new_text_len
            )

            return new_vowel_consonant_rate

        return None


class SymbolRate:
    def __init__(self,
                 all_symbol_rate: dict,
                 vowel_consonant_rate: VowelConsonantRate,
                 text_len: int):
        self.all_symbol_rate = all_symbol_rate
        self.vowel_consonant_rate = vowel_consonant_rate
        self.text_len = text_len

    def __dict__(self):
        rate_dict = {
            "all_symbol_rate": self.all_symbol_rate,
            "vowel_consonant_rate": self.vowel_consonant_rate.__dict__(),
            "text_len": self.text_len
        }

        return rate_dict

    def __add__(self, other):
        if type(other) == SymbolRate:
            new_symbol_rate = self.add_symbol_rate(other)
            new_vowel_consonant_rate = self.vowel_consonant_rate + other.vowel_consonant_rate
            new_text_len = self.text_len + other.text_len

            new_rate = SymbolRate(
                new_symbol_rate,
                new_vowel_consonant_rate,
                new_text_len
            )

            return new_rate

        return None

    def add_symbol_rate(self, other):
        new_text_len = self.text_len + other.text_len
        new_symbol_rate = {}
        all_symbol_count = {}

        def add_to_all_symbol_count(all_symbol_rate: dict, text_len: int):
            for symbol_char in all_symbol_rate.keys():
                if symbol_char in all_symbol_count.keys():
                    all_symbol_count[symbol_char] += all_symbol_rate[symbol_char] * text_len
                else:
                    all_symbol_count[symbol_char] = all_symbol_rate[symbol_char] * text_len

        add_to_all_symbol_count(self.all_symbol_rate, self.text_len)
        add_to_all_symbol_count(other.all_symbol_rate, other.text_len)

        for symbol in all_symbol_count.keys():
            new_symbol_rate[symbol] = all_symbol_count[symbol] / new_text_len

        return new_symbol_rate


def vowel_consonant_from_dict(rate_dict: dict) -> VowelConsonantRate:
    vowel_consonant_rate = VowelConsonantRate(
        rate_dict["vowels_rate"],
        rate_dict["consonant_rate"],
        rate_dict["text_len"]
    )

    return vowel_consonant_rate


def symbol_rate_from_dict(rate_dict: dict) -> SymbolRate:
    symbol_rate = SymbolRate(
        rate_dict["all_symbol_rate"],
        vowel_consonant_from_dict(rate_dict["vowel_consonant_rate"]),
        rate_dict["text_len"]
    )

    return symbol_rate
