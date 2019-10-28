import requests as rq 
from bs4 import BeautifulSoup as bs

url = 'https://esir.gov.spb.ru/'

html = rq.get(url, verify=False)

bso = bs(html.text, 'html.parser')

#print(bso)

kol_li = bso.find('ul',{'class':'catalog-category'}).findAll('li')

for li in kol_li:
	print(li.getText().strip())
