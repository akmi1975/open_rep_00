from .models import Org, GorRayon, Nsp, Otrasl, PodOtrasl, orgContact

def basic_filtr_or(vid_sel, vid_1_id, pod_vid_1_id):
	
	ME_VID1_ID = vid_1_id
	ME_PODVID1_ID = pod_vid_1_id
	#ME_VID2_ID = rayon_id
	#ME_PODVID2_ID = nsp_id

	if vid_sel == 0:
		vid_1 = GorRayon.objects.filter(org__rayon__gt=0).distinct()
		vid_2 = Otrasl.objects.filter(org__rayon__gt=ME_VID1_ID).filter(org__otrasl__gt=0).distinct()
		pod_vid_1 = Nsp.objects.filter(rayon=ME_VID1_ID).filter(org__nsp__gt=0).distinct()
		pod_vid_2 = PodOtrasl.objects.filter(org__pod_otrasl__gt=0).distinct()
		return {'href_vid_sel':'/1/0/0/0/0/', 'vid_sel':0, 'vid_1':vid_1, 'vid_2':vid_2, 'pod_vid_1':pod_vid_1,'pod_vid_2':pod_vid_2, 'me_vid1':ME_VID1_ID}
	elif vid_sel == 1:
		vid_1 = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
		vid_2 = GorRayon.objects.filter(org__rayon__gt=0).distinct()
		pod_vid_1 = PodOtrasl.objects.filter(otrasl=ME_VID1_ID).filter(org__pod_otrasl__gt=0).distinct()
		pod_vid_2 = Nsp.objects.filter(org__nsp__gt=0).distinct()
		return {'href_vid_sel':'/0/0/0/0/0/', 'vid_sel':1, 'vid_1':vid_1, 'vid_2':vid_2, 'pod_vid_1':pod_vid_1,'pod_vid_2':pod_vid_2, 'me_vid1':ME_VID1_ID}