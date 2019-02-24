import requests
import xml.etree.ElementTree


parameters = { 'key': "84AD3BB0C4BF3809A9CF3CCA68FAF946", 'q': '사과', 'part': 'word', 'translated': 'y',\
     'trans_lang': '1'} 
url = "https://krdict.korean.go.kr/api/search"
url1 = requests.get(url, params = parameters)

content = url1.text


fl = open("data.xml",'w')
fl.write(content)
fl.close()