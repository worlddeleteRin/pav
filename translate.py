import polib
from deep_translator import MyMemoryTranslator
import time
import boto3

languages = {
    # 'en': '/Users/noname/work/ilya/pav/locale/en/LC_MESSAGES/django.po',
    'uk': '/Users/noname/work/ilya/pav/locale/ua/LC_MESSAGES/django.po'
}
AMAZON_ACCESS_KEY = 'AKIAIHXSJ5NCFE7BXKQA'
AMAZON_SECRET_KEY = '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'


def translate():
    print('Initializing amazon client...')
    client = boto3.client('translate', 
    aws_access_key_id = AMAZON_ACCESS_KEY,
    aws_secret_access_key = AMAZON_SECRET_KEY,
    region_name = 'us-east-1')
    print('Amazon client initialized success!')
    print('Starting translate...')
    global languages
    for lang in languages:
        file_path = languages[lang]
        file = polib.pofile(file_path)
        for item in file: 
            to_translate = item.msgid
            item.msgstr = translate_text(client, lang, to_translate)
            print(to_translate, '\n', item.msgstr)
            # time.sleep(1)
        file.save(file_path)
    print('Finish translate...')


def translate_text(client, target, text):
    response = client.translate_text(
    Text=text,
    SourceLanguageCode='ru',
    TargetLanguageCode=target,
    )   
    return response['TranslatedText']


if __name__ == '__main__':
    translate()