#
# test git 
#
#import requests as rq 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os.path

phantomjs_path = "C:\\$MY$\\OpenData\\web_driver\\phantomjs.exe"

url = 'http://www.abyalil.ru/openrepublic/'


browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
browser.get(url)
html = browser.page_source
#html = rq.get(url, verify=False)

bso = bs(html, 'html.parser')

#print(bso)

kol_li = bso.find('div',{'class':'l-menu'}).find('ul').findAll('li',{'class':'accordion'})
#print(kol_li)


for li in kol_li:
	print(li.getText().strip())
