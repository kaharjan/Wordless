#
# Wordless: Conversion
#
# Copyright (C) 2018 Ye Lei (叶磊) <blkserene@gmail.com>
#
# License Information: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#

def to_lang_code(main, lang_text):
    if type(lang_text) == list:
        return [main.settings_global['langs'][item] for item in lang_text]
    else:
        return main.settings_global['langs'][lang_text]

def to_lang_text(main, lang_code):
    langs = {lang_code: lang_text for lang_text, lang_code in main.settings_global['langs'].items()}

    if type(lang_code) == list:
        return [langs[item] for item in lang_code]
    else:
        return langs[lang_code]

def to_iso_639_3(main, lang_code):
    for lang_code_639_3, lang_code_639_2 in main.settings_global['lang_codes'].items():
        if lang_code == lang_code_639_2:
            return lang_code_639_3

def to_iso_639_1(main, lang_code):
    return main.settings_global['lang_codes'][lang_code]

def to_ext_text(main, ext_code):
    return main.settings_global['file_exts'][ext_code].split(' (')[0]

def to_encoding_code(main, encoding_text):
    return main.settings_global['file_encodings'][encoding_text]

def to_encoding_text(main, encoding_code):
    for text, code in main.settings_global['file_encodings'].items():
        if encoding_code == code:
            return text

def to_universal_tagset(main, tagset, tag):
    tagset = main.settings_global['tagsets'][tagset]

    with open(f'tagsets/{tagset}.txt', 'r', encoding = 'utf_8') as f:
        tagset_mapping = {line.rstrip().split()[0]: line.rstrip().split()[1]
                          for line in f
                          if line.find('\t') > -1}

    return tagset_mapping[tag]
