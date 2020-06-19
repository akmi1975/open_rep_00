'''
	Добавляем организации
'''

from time import sleep
#from django.contrib.auth.models import User, Group
from rep_test_00.models import Org, Otrasl, Regions, GorRayon, PodOtrasl, Nsp

# =====================================================
CSV_FILE = 'org_template_org_file_karach_fap.csv'
# =====================================================


def orgs_from_file(fn):
	with open(fn) as f:
		lines = f.read().splitlines()
	return lines

def add_orgs(fn):
	orgs = orgs_from_file(fn)
	for org in orgs:
		mas_org = org.split(';')
		otrasl = mas_org[0]
		pod_otrasl = mas_org[1]
		region = mas_org[2]
		rayon = mas_org[3]
		nsp = mas_org[4]
		inn = mas_org[5]
		name = mas_org[6]
		name_short = mas_org[7]
		okved = mas_org[8]
		okved_name = mas_org[9]

		try:
			o1 = Org(inn = inn, name = name, nsp = Nsp.objects.get(pk = nsp), rayon = GorRayon.objects.get(pk = rayon), region = Regions.objects.get(pk = region), name_short = name_short, okved = okved, okved_name = okved_name, otrasl = Otrasl.objects.get(pk = otrasl), pod_otrasl = PodOtrasl.objects.get(pk = pod_otrasl))
			#user.groups.add(group) # add by id
			o1.save()
		except Exception as ex:
			print(' error '+ str(inn) + ' ' + str(ex))


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