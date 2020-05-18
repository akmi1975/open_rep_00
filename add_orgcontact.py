

'''
	Добавляем адреса организаций
'''

from time import sleep
#from django.contrib.auth.models import User, Group
from rep_test_00.models import Org, orgContact

# =====================================================
CSV_FILE = 'orgcontact_zag_09.csv'
# =====================================================


def orgs_from_file(fn):
	with open(fn) as f:
		lines = f.read().splitlines()
	return lines

def add_orgs(fn):
	orgs = orgs_from_file(fn)
	for org in orgs:
		mas_org = 	org.split(';')
		adres = 	mas_org[0]
		telefone = 	mas_org[1]
		email = 	mas_org[2]
		url = 		mas_org[3]
		org_id = 	mas_org[4]
		vremya = 	mas_org[5]

		try:
			o1 = orgContact(adres = adres, telefone = telefone, email = email, org_id = org_id, url = url, vremya = vremya)
			#user.groups.add(group) # add by id
			o1.save()
		except Exception as ex:
			print(' error '+ str(org_id) + ' ' + str(ex))


def all():
	global CSV_FILE
	print('ready! \nadd ORGS ...')
	add_orgs(CSV_FILE)
	print('ready!')


'''
if __name__ == '__main__':
	main()
	test_00()
'''










