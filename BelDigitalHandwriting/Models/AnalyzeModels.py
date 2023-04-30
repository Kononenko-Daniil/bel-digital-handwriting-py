from .SymbolModels import *
from .WordSentenceModels import *


class BelDHAnalyze:
    def __init__(self,
                 text_len: int,
                 symbol_rate: SymbolRate,
                 word_sentence_rate: WordSentenceRate):
        self.text_len = text_len
        self.symbol_rate = symbol_rate
        self.word_sentence_rate = word_sentence_rate

    def __dict__(self):
        analyze_dict = {
            "text_len": self.text_len,
            "symbol_rate": self.symbol_rate.__dict__(),
            "word_sentence_rate": self.word_sentence_rate.__dict__()
        }

        return analyze_dict

    def __add__(self, other):
        if type(other) == BelDHAnalyze:
            new_analyze = BelDHAnalyze(
                self.text_len + other.text_len,
                self.symbol_rate + other.symbol_rate,
                self.word_sentence_rate + other.word_sentence_rate
            )

            return new_analyze

        return None


def bel_dh_analyze_from_dict(analyze_dict: dict) -> BelDHAnalyze:
    bel_dh_analyze = BelDHAnalyze(
        analyze_dict['text_len'],
        symbol_rate_from_dict(analyze_dict['symbol_rate']),
        word_sentence_rate_from_dict(analyze_dict['word_sentence_rate'])
    )

    return bel_dh_analyze

