import polib
from deep_translator import MyMemoryTranslator
import time

languages = {
    'en': '/Users/noname/work/ilya/pav/locale/en/LC_MESSAGES/django.po',
    'ukrainian': '/Users/noname/work/ilya/pav/locale/ua/LC_MESSAGES/djnago.po'
}


def translate():
    print('Starting translate...')
    global languages
    for lang in languages:
        file_path = languages[lang]
        file = polib.pofile(file_path)
        for item in file: 
            to_translate = item.msgid
            item.msgstr = translate_text(lang, to_translate)
            print(to_translate, '\n', item.msgstr)
            time.sleep(3)
        file.save(file_path)
    print('Finish translate...')


def translate_text(target, text):
    resp = MyMemoryTranslator(
    source = 'ru',
    target = target
    ).translate(text)
    return resp


if __name__ == '__main__':
    translate()