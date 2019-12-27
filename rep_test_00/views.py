from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Org, GorRayon, Nsp, Otrasl, PodOtrasl

ME_OTRASL_ID = 0
ME_PODOTRASL_ID = 0

def index(request):
	#template = loader.get_template('org_selector/index.html')
	Rayons = GorRayon.objects.filter(org__rayon__gt=0).distinct()
	Nsps = Nsp.objects.filter(org__nsp__gt=0).distinct()
	Otrasls = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
	PodOtrasls = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()
	#Orgs = Org.objects.all()
	context = {'Rayons':Rayons, 'Nsps':Nsps, 'Otrasls':Otrasls, 'PodOtrasls':PodOtrasls }
	#context = {'Orgs':Orgs}
	#return HttpResponse(template.render(context, request))
	return render(request, 'org_selector/index.html', context)

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


