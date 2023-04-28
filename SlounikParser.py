import xml.etree.ElementTree as ET
import os
import re

speech_parts = {
    "N": "nazounik.txt",
    "A": "prymetnik.txt",
    "M": "lychebnik.txt",
    "S": "zaymenik.txt",
    "V": "dzeyaslou.txt",
    "P": "dzeeprymetnik.txt",
    "R": "prysloue.txt",
    "C": "zluchnik.txt",
    "I": "prynazounik.txt",
    "E": "chastica.txt",
    "Y": "vyklichnik.txt",
    "Z": "pabochnae_slova.txt",
    "W": "predycatiu.txt",
}

speech_parts_str = {
    "nazounik.txt": "",
    "prymetnik.txt": "",
    "lychebnik.txt": "",
    "zaymenik.txt": "",
    "dzeyaslou.txt": "",
    "dzeeprysloue.txt": "",
    "dzeeprymetnik.txt": "",
    "prysloue.txt": "",
    "zluchnik.txt": "",
    "prynazounik.txt": "",
    "chastica.txt": "",
    "vyklichnik.txt": "",
    "pabochnae_slova.txt": "",
    "predycatiu.txt": ""
}

slounik_dir = "slouniki"
speech_parts_parsed_dir = "BelDigitalHandwriting/slouniki_parsed"


def get_word_target_filepath(xml_paradigm):
    tag_attr = xml_paradigm.attrib['tag']
    tag_speech_part = tag_attr[0]

    try:
        filepath = speech_parts[tag_speech_part]
        return tag_speech_part, filepath
    except:
        return None, None


def clean_word(word: str):
    try:
        word = re.sub(r"\+", "", word)
    except:
        pass

    return word


def add_word_forms_to_dataset(word_forms, path):
    for word in word_forms.keys():
        if word_forms[word] == "DZ":
            speech_parts_str["dzeeprysloue.txt"] += "{0}#".format(word)
        else:
            speech_parts_str[path] += "{0}#".format(word)


def get_word_forms(xml_paradigm, sp_part):
    word_forms = {}

    for word_form in xml_paradigm.iter("Form"):
        try:
            form_tag = word_form.attrib['tag']
            word = clean_word(word_form.text)
            if sp_part == "V":
                if form_tag[1] == 'G':
                    word_forms[word] = "DZ"
                    continue
            word_forms[word] = ""
        except:
            pass

    return word_forms


def save_parsed_data():
    for parsed_filepath in speech_parts_str.keys():
        file = open(
            os.path.join(speech_parts_parsed_dir, parsed_filepath),
            'w',
            encoding='utf-8'
        )

        file.write(speech_parts_str[parsed_filepath])
        file.close()


for slounik_name in os.listdir(slounik_dir):
    slounik_path = os.path.join(slounik_dir, slounik_name)

    if os.path.isfile(slounik_path):
        print(slounik_path)

        slounik_tree = ET.parse(slounik_path)
        slounik_root = slounik_tree.getroot()
        for paradigm in slounik_root.iter("Paradigm"):
            if "tag" in paradigm.attrib.keys():
                speech_part, speech_part_filepath = get_word_target_filepath(paradigm)
                if speech_part and speech_part_filepath:
                    paradigm_forms = get_word_forms(paradigm, speech_part)
                    add_word_forms_to_dataset(paradigm_forms, speech_part_filepath)
                    # print(speech_parts_str)

save_parsed_data()
