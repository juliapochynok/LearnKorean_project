import requests
import xml.etree.ElementTree
import random

def make_wordimfo_file(needed_word, file):
     '''
     '''
     parameters = { 'key': "84AD3BB0C4BF3809A9CF3CCA68FAF946", 'q': needed_word, 'part': 'word', 'translated': 'y',\
          'trans_lang': '1'} 
     url = "https://krdict.korean.go.kr/api/search"
     url1 = requests.get(url, params = parameters)

     content = url1.text

     fl = open(file,'w')
     fl.write(content)
     fl.close()

def get_translation(file):
    '''
    '''
    fl = open(file)
    tx = fl.read()
    xmlData = str(tx)
    fl.close()

    translation = []
    import xml.etree.ElementTree as ET
    xml = ET.fromstring(xmlData)

    for table in xml.getiterator('channel'):
        for child in table[7][5][2]:
            translation.append(child.text.strip())
    return translation


def form_words_dict():
    '''
    '''
    translated_words = {}
    korean_word = '사과'
    kor_word = '오다'
    make_wordimfo_file(korean_word, 'data_example.xml')
    translation = get_translation('data_example.xml')
    translated_words[korean_word] = translation
    make_wordimfo_file(kor_word, 'data_example.xml')
    translation = get_translation('data_example.xml')
    translated_words[kor_word] = translation
    return translated_words


def random_word(words):
    '''
    '''
    word =  random.choice([key for key in words])
    return word

if __name__ == "__main__":
    m = form_words_dict()
    print(m)
    print("Random word: ")
    print(random_word(m))