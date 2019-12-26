'''
	Добавляем организации

'''


from time import sleep
#from django.contrib.auth.models import User, Group
from rep_test_00.models import Org, Otrasl, Regions, GorRayon, PodOtrasl, Nsp


def orgs_from_file():
	with open('test.csv', 'r') as f:
		lines = f.read().splitlines()
	return lines
	#for line in lines:
	#	print(line)
	#	sleep(1)


def add_orgs():
	orgs = orgs_from_file()
	for org in orgs:
		mas_org = org.split(';')
		inn = mas_org[0]
		name = mas_org[1]
		nsp = mas_org[2]
		rayon = mas_org[3]
		region = mas_org[4]
		name_short = mas_org[5]
		okved = mas_org[6]
		okved_name = mas_org[7]
		otrasl = mas_org[8]
		pod_otrasl = mas_org[9]
		#print(mas_org)
		try:
			o1 = Org(inn = inn, name = name, nsp = Nsp.objects.get(pk = nsp), rayon = GorRayon.objects.get(pk = rayon), region = Regions.objects.get(pk = region), name_short = name_short, okved = okved, okved_name = okved_name, otrasl = Otrasl.objects.get(pk = otrasl), pod_otrasl = PodOtrasl.objects.get(pk = pod_otrasl))
			#user.groups.add(group) # add by id
			o1.save()
		except Exception as ex:
			print(' error '+ str(inn) + ' ' + str(ex))


def all():
	print('ready! \n add ORGS ...')
	add_orgs()
	print('ready!')


'''
if __name__ == '__main__':
	main()
	test_00()
'''