'''
	Добавляем в организации контактную информацию

'''


from time import sleep
#from django.contrib.auth.models import User, Group
from rep_test_00.models import Org, orgContact


def orgs_from_file():
	with open('contact.csv', 'r') as f:
		lines = f.read().splitlines()
	return lines
	#for line in lines:
	#	print(line)
	#	sleep(1)


def add_orgs():
	orgs = orgs_from_file()
	for org_l in orgs:
		mas_org = org_l.split(';')
		org = mas_org[0]
		inn = mas_org[1]
		adres = mas_org[3]
		tel = mas_org[4]
		url = mas_org[5]
		email = mas_org[6]
		vremya = mas_org[7]
		#print(mas_org)
		try:
			o1 = orgContact(org = Org.objects.get(pk = org), adres = adres, telefone = tel, email = email, url = url, vremya = vremya)
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