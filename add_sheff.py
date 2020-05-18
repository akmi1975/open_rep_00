

'''
	Добавляем руководителей организаций
'''

from time import sleep
#from django.contrib.auth.models import User, Group
from rep_test_00.models import Org, Sheff

# =====================================================
CSV_FILE = 'sheff_zag_09.csv'
# =====================================================


def orgs_from_file(fn):
	with open(fn) as f:
		lines = f.read().splitlines()
	return lines

def add_orgs(fn):
	orgs = orgs_from_file(fn)
	for org in orgs:
		mas_org = 	org.split(';')
		# ===================================================
		fm = 		mas_org[0]
		im = 		mas_org[1]
		ot = 		mas_org[2]
		dolzhn = 	mas_org[3]
		inn_ruk = 	mas_org[4]
		doc = 		mas_org[5]
		nom_doc = 	mas_org[6]
		dt_doc = 	mas_org[7]
		active = 	mas_org[8]
		org_id = 	mas_org[9]

		try:
			o1 = Sheff(fm = fm, im = im, ot = ot, dolzhn = dolzhn, inn_ruk = inn_ruk, doc = doc, nom_doc = nom_doc, dt_doc = dt_doc, active = active, org_id = org_id)
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










