#https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D0%B0%D0%B7%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD

import requests as rq
from bs4 import BeautifulSoup as bs


def s_f(stka):
	with open('file.txt', 'a') as f:
		f.write(stka + '\n')


url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%80%D0%B0%D1%87%D0%B0%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%BA%D1%80%D1%83%D0%B3'

html = rq.get(url)
bso = bs(html.text, 'html.parser')

tb = bso.findAll('table')

nom_tab = 5

print(len(tb))
print(len(tb[nom_tab].findAll('tr')))


for tr in tb[nom_tab].findAll('tr'):
	try:
		s = tr.findAll('td')[2].text.strip()
		s_2 = tr.findAll('td')[1].text.strip()
		print(s + ' ' + s_2)
		s_f(s + ' ' + s_2)
	except:
		pass



