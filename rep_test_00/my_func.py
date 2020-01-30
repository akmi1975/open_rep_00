from .models import Org, GorRayon, Nsp, Otrasl, PodOtrasl, orgContact, Sheff
#from django.db.models import Q
from django.core.paginator import Paginator


def basic_filtr_or(request, vid_sel, vid_1_id, pod_vid_1_id, vid_2_id, pod_vid_2_id):

	ME_VID1_ID = vid_1_id
	ME_PODVID1_ID = pod_vid_1_id
	ME_VID2_ID = vid_2_id
	ME_PODVID2_ID = pod_vid_2_id

	orgs = Org.objects.all()
	OrgContact = orgContact.objects.all()

	if vid_sel == 0:
		vid_1 = GorRayon.objects.filter(org__rayon__gt=0).distinct()
		vid_2 = Otrasl.objects.filter(org__rayon__exact=ME_VID1_ID).filter(org__otrasl__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			vid_2 = vid_2.filter(org__nsp__exact=ME_PODVID1_ID)
		pod_vid_1 = Nsp.objects.filter(rayon=ME_VID1_ID).filter(org__nsp__gt=0).distinct()
		pod_vid_2 = PodOtrasl.objects.filter(org__rayon__exact=ME_VID1_ID).filter(otrasl=ME_VID2_ID).filter(org__pod_otrasl__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			pod_vid_2 = pod_vid_2.filter(org__nsp__exact=ME_PODVID1_ID)
			orgs = orgs.filter(nsp=ME_PODVID1_ID)
			OrgContact = OrgContact.filter(org__nsp__exact=ME_PODVID1_ID)
		vs = 1
		if ME_VID1_ID != 0:
			orgs = orgs.filter(rayon=ME_VID1_ID)
			OrgContact = OrgContact.filter(org__rayon__exact=ME_VID1_ID)
		if ME_VID2_ID != 0:
			orgs = orgs.filter(otrasl=ME_VID2_ID)
			OrgContact = OrgContact.filter(org__otrasl__exact=ME_VID2_ID)
		if ME_PODVID2_ID != 0:
			orgs = orgs.filter(pod_otrasl=ME_PODVID2_ID)
			OrgContact = OrgContact.filter(org__pod_otrasl__exact=ME_PODVID2_ID)
		name_vid = ['Город\\Район', 'Отрасль']
		
	elif vid_sel == 1:
		vid_1 = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
		vid_2 = GorRayon.objects.filter(org__otrasl__exact=ME_VID1_ID).filter(org__rayon__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			vid_2 = vid_2.filter(org__pod_otrasl__exact=ME_PODVID1_ID)
		pod_vid_1 = PodOtrasl.objects.filter(otrasl=ME_VID1_ID).filter(org__pod_otrasl__gt=0).distinct()
		pod_vid_2 = Nsp.objects.filter(org__otrasl__exact=ME_VID1_ID).filter(rayon=ME_VID2_ID).filter(org__nsp__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			pod_vid_2 = pod_vid_2.filter(org__pod_otrasl__exact=ME_PODVID1_ID)
			orgs = orgs.filter(pod_otrasl=ME_PODVID1_ID)
			OrgContact = OrgContact.filter(org__pod_otrasl__exact=ME_PODVID1_ID)
		vs = 0
		if ME_VID1_ID != 0:
			orgs = orgs.filter(otrasl=ME_VID1_ID)
			OrgContact = OrgContact.filter(org__otrasl__exact=ME_VID1_ID)
		if ME_VID2_ID != 0:
			orgs = orgs.filter(rayon=ME_VID2_ID)
			OrgContact = OrgContact.filter(org__rayon__exact=ME_VID2_ID)
		if ME_PODVID2_ID != 0:
			orgs = orgs.filter(nsp=ME_PODVID2_ID)
			OrgContact = OrgContact.filter(org__nsp__exact=ME_PODVID2_ID)
		name_vid = ['Отрасль','Город\\Район']


	paginator = Paginator(orgs, 1)
	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1
	page = paginator.get_page(page_num)

	sheff = Sheff.objects.filter(org=page.object_list[0]).filter(active=True)[0]

	return {'href_vid_sel':'/' + str(vs) + '/0/0/0/0/', 'vid_sel':vid_sel, 'vid_1':vid_1, 'vid_2':vid_2, 'pod_vid_1':pod_vid_1,'pod_vid_2':pod_vid_2, 'me_vid1':ME_VID1_ID, 'me_podvid1':ME_PODVID1_ID, 'me_vid2':ME_VID2_ID, 'me_podvid2':ME_PODVID2_ID, 'Orgs':page.object_list, 'OrgContact':OrgContact, 'page':page, 'name_vid':name_vid, 'sheff':sheff}

