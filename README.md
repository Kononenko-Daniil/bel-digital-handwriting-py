# bel-digital-handwriting-py
**bel-digital-handwriting-py** - гэта Python бібліятэка, з дапамогай якой вы можаце хутка
аналізаваць беларускія тэксты па спецыяльных крытэрыях. 

```python
import BelDigitalHandwriting.BelDHAnalyser as BelDHAnalyser

text_file = open("text.txt", "r", encoding="utf-8")
text = text_file.read()

text_info = BelDHAnalyser.analyse_text(text)
```

## Як карыстацца гэтай бібліятэкай
Каб пачаць выкарыстоўваць **bel-digital-handwriting-py**, вы павінны ўсталяваць бібліятэку
праз PIP:

```commandline
pip install bel-digital-handwriting-py
```

## Спасылкі на выкарыстоўваемые матэрыялы
 - У праекце выкарыстоўваюцца слоўнікі Беларускага N-корпусу. 
Спасылка на іх рэпазітар Github - [GrammarDB](https://github.com/Belarus/GrammarDB). 
Граматычная база распаўсюджвацца па ліцэнзіі [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Спасылка на ліцэнзію Граматычнай базы - [CC BY-SA 4.0](https://github.com/Belarus/GrammarDB/blob/master/docs/LICENSE.txt)