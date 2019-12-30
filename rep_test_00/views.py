from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Org, GorRayon, Nsp, Otrasl, PodOtrasl, orgContact
#from django.db.models import Q

ME_OTRASL_ID = 0
ME_PODOTRASL_ID = 0
ME_RAYON_ID = 0
ME_NSP_ID = 0

def index(request):
	#template = loader.get_template('org_selector/index.html')
	Rayons = GorRayon.objects.filter(org__rayon__gt=0).distinct()
	Nsps = Nsp.objects.filter(org__nsp__gt=0).distinct()
	Otrasls = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
	PodOtrasls = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()

	#links: https://djbook.ru/rel1.7/topics/db/queries.html
	Orgs = Org.objects.all()[:5]
	#Orgs = Org.objects.all()
	#context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls }
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls, 'me_otr':ME_OTRASL_ID, 'me_podotr':ME_PODOTRASL_ID, 'me_ray': ME_RAYON_ID, 'me_nsp':ME_NSP_ID, 'Orgs':Orgs }

	#context = {'Orgs':Orgs}
	#return HttpResponse(template.render(context, request))
	return render(request, 'org_selector/index_1.html', context)


def by_otrasl(request, otrasl_id, podotrasl_id, rayon_id, nsp_id):
	ME_OTRASL_ID = otrasl_id
	ME_PODOTRASL_ID = podotrasl_id
	ME_RAYON_ID = rayon_id
	ME_NSP_ID = nsp_id

	Rayons = GorRayon.objects.filter(org__rayon__gt=0).distinct()
	Nsps = Nsp.objects.filter(org__nsp__gt=0).distinct()
	Otrasls = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
	PodOtrasls = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()

	Orgs = Org.objects.all()

	#links: https://djbook.ru/rel1.8/topics/db/queries.html

	t_otr, t_pod, t_ray, t_nsp = '', '', '', ''

	#t_vid_sort = ['по отраслям', 'по районам']

	if ME_OTRASL_ID > 0:
		Orgs = Orgs.filter(otrasl=ME_OTRASL_ID)
		#if vid_sort == 0:
		Rayons = Rayons.filter(org__otrasl=ME_OTRASL_ID)
		Nsps = Nsps.filter(org__otrasl=ME_OTRASL_ID)
		t_otr = Otrasl.objects.get(id=ME_OTRASL_ID)
	if ME_PODOTRASL_ID > 0:
		Orgs = Orgs.filter(pod_otrasl=ME_PODOTRASL_ID)
		#if vid_sort == 0:
		Rayons = Rayons.filter(org__pod_otrasl=ME_PODOTRASL_ID)
		Nsps = Nsps.filter(org__pod_otrasl=ME_PODOTRASL_ID)
		t_pod = PodOtrasl.objects.get(id=ME_PODOTRASL_ID)
	if ME_RAYON_ID > 0:
		Orgs = Orgs.filter(rayon=ME_RAYON_ID)
		t_ray = GorRayon.objects.get(id=ME_RAYON_ID)
		#if vid_sort == 1:
		#	Otrasls = Otrasls.filter(org__rayon=ME_RAYON_ID)
		#	PodOtrasls = PodOtrasls.filter(org__rayon=ME_RAYON_ID)
	if ME_NSP_ID > 0:
		Orgs = Orgs.filter(nsp=ME_NSP_ID)
		t_nsp = Nsp.objects.get(id=ME_NSP_ID)
		#if vid_sort == 1:
		#	Otrasls = Otrasls.filter(org__nsp=ME_NSP_ID)
		#	PodOtrasls = PodOtrasls.filter(org__nsp=ME_NSP_ID)
	test = [t_otr, t_pod, t_ray, t_nsp]

	OrgContact = orgContact.objects.all()
	#if vid_sort == 0:
	#	mas_vid_sort = [1, t_vid_sort[1]]
	#else:
	#	mas_vid_sort = [0, t_vid_sort[0]]

	#Orgs = Org.objects.all()
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls, 'me_otr':ME_OTRASL_ID, 'me_podotr':ME_PODOTRASL_ID, 'me_ray': ME_RAYON_ID, 'me_nsp':ME_NSP_ID, 'Orgs':Orgs, 'test':test, 'OrgContact':OrgContact }

	return render(request, 'org_selector/index_1.html', context)

