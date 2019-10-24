#https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D0%B0%D0%B7%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD

import requests as rq
from bs4 import BeautifulSoup as bs


def s_f(stka):
	with open('file.txt', 'a') as f:
		f.write(stka + '\n')


url = 'https://ru.wikipedia.org/wiki/%D0%90%D0%B4%D1%8B%D0%B3%D0%B5-%D0%A5%D0%B0%D0%B1%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD'

html = rq.get(url)
bso = bs(html.text, 'html.parser')

tb = bso.findAll('table')

print(len(tb))
print(len(tb[4].findAll('tr')))


for tr in tb[4].findAll('tr'):
	try:
		print(tr.findAll('td')[2].text.strip())
		#s_f(tr.findAll('td')[2].text.strip())
	except:
		pass



