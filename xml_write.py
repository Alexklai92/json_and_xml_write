from pprint import pprint 
import xml.etree.ElementTree as ET
from operator import itemgetter

tree = ET.parse('newsafr.xml')
root = tree.getroot()

test = list()
word_list = list()

xml_desc = root.findall('channel/item/description')
for xmli in xml_desc:
	for j in xmli.text.split():
		if len(j) >= 6:
			word_list.append(j)

result = {i: word_list.count(i) for i in word_list}
count = 0
top_words = sorted(result.items(), key=itemgetter(1))
top_words.reverse()
for w in top_words:
	count += 1
	if count == 10:
		break
	print(f'Место: {count}, слово "{w[0]}", вхождений {w[1]}')
