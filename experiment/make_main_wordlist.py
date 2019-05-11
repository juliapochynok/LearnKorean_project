from get_xml import make_wordimfo_file

def get_words_to_learn(file):
    '''
    '''
    fl = open(file)
    words = fl.readlines()
    fl.close()
    for word in range(len(words)):
        words[word] = words[word].replace('\n', '')
    return words

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
    n = 0
    fl = open('tanslations.txt', 'w')
    korean_words = get_words_to_learn('words.txt')
    for every in korean_words:
        make_wordimfo_file(every, 'data.xml')
        translation = get_translation('data.xml')
        translated_words[every] = translation
        n += 1
        fl.write(str(n) + "," + every + "," + translation[0] + "," \
            + translation[1] + "," + translation[2] + "\n")
    fl.close()
    return translated_words


if __name__ == "__main__":
    print(form_words_dict())
    