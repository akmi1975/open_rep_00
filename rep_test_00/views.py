from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Org, GorRayon, Nsp, Otrasl, PodOtrasl

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
	#Orgs = Org.objects.all()
	#context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls }
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls, 'me_otr':ME_OTRASL_ID, 'me_podotr':ME_PODOTRASL_ID, 'me_ray': ME_RAYON_ID, 'me_nsp':ME_NSP_ID }

	#context = {'Orgs':Orgs}
	#return HttpResponse(template.render(context, request))
	return render(request, 'org_selector/index_1.html', context)

def by_otrasl(request, otrasl_id):
	ME_OTRASL_ID = otrasl_id
	#ME_PODOTRASL_ID = podotrasl_id

	Rayons = GorRayon.objects.filter(org__rayon__gt=0).distinct()
	Nsps = Nsp.objects.filter(org__nsp__gt=0).distinct()
	Otrasls = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
	PodOtrasls = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()
	#Orgs = Org.objects.all()
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls, 'me_otr':ME_OTRASL_ID, 'me_podotr':ME_PODOTRASL_ID }

	return render(request, 'org_selector/index.html', context)

def by_otrasl_2(request, otrasl_id, podotrasl_id):
	ME_OTRASL_ID = otrasl_id
	ME_PODOTRASL_ID = podotrasl_id

	Rayons = GorRayon.objects.filter(org__rayon__gt=0).distinct()
	Nsps = Nsp.objects.filter(org__nsp__gt=0).distinct()
	Otrasls = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
	PodOtrasls = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()
	#Orgs = Org.objects.all()
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls, 'me_otr':ME_OTRASL_ID, 'me_podotr':ME_PODOTRASL_ID }

	return render(request, 'org_selector/index.html', context)

def by_otrasl_4(request, otrasl_id, podotrasl_id, rayon_id, nsp_id):
	ME_OTRASL_ID = otrasl_id
	ME_PODOTRASL_ID = podotrasl_id
	ME_RAYON_ID = rayon_id
	ME_NSP_ID = nsp_id

	Rayons = GorRayon.objects.filter(org__rayon__gt=0).distinct()
	Nsps = Nsp.objects.filter(org__nsp__gt=0).distinct()
	Otrasls = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
	PodOtrasls = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()

	if ME_PODOTRASL_ID == 0 and ME_NSP_ID == 0:
		Orgs = Org.objects.filter(otrasl=ME_OTRASL_ID).filter(rayon=ME_RAYON_ID)
	elif ME_PODOTRASL_ID != 0 and ME_NSP_ID == 0:
		Orgs = Org.objects.filter(otrasl=ME_OTRASL_ID).filter(pod_otrasl=ME_PODOTRASL_ID).filter(rayon=ME_RAYON_ID)
	elif ME_PODOTRASL_ID == 0 and ME_NSP_ID != 0:
		Orgs = Org.objects.filter(otrasl=ME_OTRASL_ID).filter(rayon=ME_RAYON_ID).filter(nsp=ME_NSP_ID)
	else:
		Orgs = Org.objects.filter(otrasl=ME_OTRASL_ID).filter(pod_otrasl=ME_PODOTRASL_ID).filter(rayon=ME_RAYON_ID).filter(nsp=ME_NSP_ID)
	#Orgs = Org.objects.all()
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls, 'me_otr':ME_OTRASL_ID, 'me_podotr':ME_PODOTRASL_ID, 'me_ray': ME_RAYON_ID, 'me_nsp':ME_NSP_ID, 'Orgs':Orgs }

	return render(request, 'org_selector/index_1.html', context)

