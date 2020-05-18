'''
	добавляем руководителей и контактную информацию

'''

import os, add_orgcontact, add_sheff

CUR_DIR = os.getcwd()

def start():

	files_list = os.listdir(CUR_DIR)

	for fn in files_list:
		if os.path.isfile(CUR_DIR + '\\' + fn) and 'csv' in fn:
			if 'orgcontact' in fn:
				print('Добавляем контактную информацию ...')
				add_orgcontact.add_orgs(CUR_DIR + '\\' + fn)
			elif 'sheff' in fn:
				print('Добавляем информацию по руководителям ...')
				add_sheff.add_orgs(CUR_DIR + '\\' + fn)






