import requests
import xml.etree.ElementTree

def make_wordinfo_file(needed_word, fle):
     '''
     Makes a API requests and writes given information to xml file

     :type needed_word: str
     :param needed_word: word which translation is needed to be found.
     :type fle: str
     :param fle: xml file that holds information.
     '''
     parameters = { 'key': "84AD3BB0C4BF3809A9CF3CCA68FAF946", 'q': needed_word,\
           'part': 'word', 'translated': 'y',\
          'trans_lang': '1'} 
     url = "https://krdict.korean.go.kr/api/search"
     url1 = requests.get(url, params = parameters)

     content = url1.text

     fl = open(fle,'w')
     fl.write(content)
     fl.close()