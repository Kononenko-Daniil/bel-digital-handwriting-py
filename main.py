import BelDigitalHandwriting.BelDHAnalyser as BelDHAnalyser
from pprint import pprint

text_file = open("test_text.txt", "r", encoding="utf-8")
text = text_file.read()
res = BelDHAnalyser.analyse_text(text)
pprint(res)
