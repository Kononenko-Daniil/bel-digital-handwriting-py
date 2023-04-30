import BelDigitalHandwriting.BelDHAnalyser as BelDHAnalyser

text_file = open("test_text.txt", "r", encoding="utf-8")
text = text_file.read()
analyze = BelDHAnalyser.analyse_text(text)

print(analyze.__dict__())

