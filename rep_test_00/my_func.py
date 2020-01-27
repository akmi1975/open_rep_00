from .models import Org, GorRayon, Nsp, Otrasl, PodOtrasl, orgContact


def basic_filtr_or(vid_sel, vid_1_id, pod_vid_1_id, vid_2_id, pod_vid_2_id):

	ME_VID1_ID = vid_1_id
	ME_PODVID1_ID = pod_vid_1_id
	ME_VID2_ID = vid_2_id
	ME_PODVID2_ID = pod_vid_2_id

	if vid_sel == 0:
		vid_1 = GorRayon.objects.filter(org__rayon__gt=0).distinct()
		vid_2 = Otrasl.objects.filter(org__rayon__exact=ME_VID1_ID).filter(org__otrasl__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			vid_2 = vid_2.filter(org__nsp__exact=ME_PODVID1_ID)
		pod_vid_1 = Nsp.objects.filter(rayon=ME_VID1_ID).filter(org__nsp__gt=0).distinct()
		pod_vid_2 = PodOtrasl.objects.filter(org__rayon__exact=ME_VID1_ID).filter(otrasl=ME_VID2_ID).filter(org__pod_otrasl__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			pod_vid_2 = pod_vid_2.filter(org__nsp__exact=ME_PODVID1_ID)
		return {'href_vid_sel':'/1/0/0/0/0/', 'vid_sel':0, 'vid_1':vid_1, 'vid_2':vid_2, 'pod_vid_1':pod_vid_1,'pod_vid_2':pod_vid_2, 'me_vid1':ME_VID1_ID, 'me_podvid1':ME_PODVID1_ID, 'me_vid2':ME_VID2_ID}
	elif vid_sel == 1:
		vid_1 = Otrasl.objects.filter(org__otrasl__gt=0).distinct()
		vid_2 = GorRayon.objects.filter(org__otrasl__exact=ME_VID1_ID).filter(org__rayon__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			vid_2 = vid_2.filter(org__pod_otrasl__exact=ME_PODVID1_ID)
		pod_vid_1 = PodOtrasl.objects.filter(otrasl=ME_VID1_ID).filter(org__pod_otrasl__gt=0).distinct()
		pod_vid_2 = Nsp.objects.filter(org__otrasl__exact=ME_VID1_ID).filter(rayon=ME_VID2_ID).filter(org__nsp__gt=0).distinct()
		if ME_PODVID1_ID != 0:
			pod_vid_2 = pod_vid_2.filter(org__pod_otrasl__exact=ME_PODVID1_ID)
		return {'href_vid_sel':'/0/0/0/0/0/', 'vid_sel':1, 'vid_1':vid_1, 'vid_2':vid_2, 'pod_vid_1':pod_vid_1,'pod_vid_2':pod_vid_2, 'me_vid1':ME_VID1_ID, 'me_podvid1':ME_PODVID1_ID, 'me_vid2':ME_VID2_ID}
