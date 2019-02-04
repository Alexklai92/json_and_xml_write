from operator import itemgetter
import json
from pprint import pprint

word_list = list()

with open('newsafr.json', encoding='utf-8', newline='') as datafile:
	json_data = json.load(datafile)

json_items = json_data['rss']['channel']['items']

for i in json_items:
	for j in i['description'].split():
		
		if len(j) > 6:
			word_list.append(j.lower())
result = {i: word_list.count(i) for i in word_list}
count = 0
top_words = sorted(result.items(), key=itemgetter(1))
top_words.reverse()
for j in top_words:
	count += 1
	if count == 11:
		break
	print(f'Место: {count}, слово "{j[0]}", вхождений {j[1]}')
	
