punctuation_marks = " !\"()*,-./:;?«°»–—“”•…№"
numbers = "0123456789"

bel_letters = "абвгдежзйклмнопрстуфхцчшыьэюяёіў’'"
rus_letters = "щъи"
eng_letters = "abcdefghijklmnopqrstuvwxyz"
deu_letters = "äöüß"
fra_letters = "éâêîôûàèùëïüÿç"

foreign_letters = rus_letters + eng_letters + deu_letters + fra_letters

accepted_symbols = punctuation_marks + numbers + foreign_letters + bel_letters

vowel_letters = "аеоуыэяяёі"
consonant_letters = "бвгджзйклмнпрстўфхцчшь"

pair_types = ["VV", "CV", "VC", "CC"]

speech_parts_gr = {
    "nazounik.txt": "N",
    "prymetnik.txt": "A",
    "lychebnik.txt": "M",
    "zaymenik.txt": "S",
    "dzeyaslou.txt": "V",
    "dzeeprysloue.txt": "D",
    "dzeeprymetnik.txt": "P",
    "prysloue.txt": "R",
    "zluchnik.txt": "C",
    "prynazounik.txt": "I",
    "chastica.txt": "E",
    "vyklichnik.txt": "Y",
    "pabochnae_slova.txt": "Z",
    "predycatiu.txt": "W"
}
