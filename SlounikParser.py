import xml.etree.ElementTree as ET
import os
import re

slounik_types = {
    "dzsl.txt": ["dzsl2007", "dzsl2013"],
    "nazounik.txt": ["nazounik2008", "nazounik2013"],
    "prym.txt": ["prym2009", "prym2013"]
}

slounik_parsed_str = {
    "dzsl.txt": "",
    "nazounik.txt": "",
    "prym.txt": ""
}

slounik_dir = "slouniki"
slounik_parsed_dir = "BelDigitalHandwriting/slouniki_parsed"


def get_word_target_filepath(xml_el):
    slouniki_attr = xml_el.attrib['slouniki']

    for parsed_filepath in slounik_types.keys():
        for slounik_type in slounik_types[parsed_filepath]:
            if slounik_type in slouniki_attr:
                return parsed_filepath

    return 0


def clean_word(word: str):
    try:
        word = re.sub(r"\+", "", word)
    except:
        print(word)

    return word


def add_word_to_parsed(word, path):
    slounik_parsed_str[path] += "{0}#".format(word)


def save_parsed_data():
    for parsed_filepath in slounik_parsed_str.keys():
        file = open(
            os.path.join(slounik_parsed_dir, parsed_filepath),
            'w',
            encoding='utf-8'
        )

        file.write(slounik_parsed_str[parsed_filepath])
        file.close()


for slounik_name in os.listdir(slounik_dir):
    slounik_path = os.path.join(slounik_dir, slounik_name)

    if os.path.isfile(slounik_path):
        print(slounik_path)

        slounik_tree = ET.parse(slounik_path)
        slounik_root = slounik_tree.getroot()
        for word_form in slounik_root.iter("Form"):
            if "slouniki" in word_form.attrib.keys():
                parsed_sln_filepath = get_word_target_filepath(word_form)
                if parsed_sln_filepath:
                    res_word = clean_word(word_form.text)
                    add_word_to_parsed(res_word, parsed_sln_filepath)

save_parsed_data()
