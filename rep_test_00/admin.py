from django.contrib import admin

# Register your models here.

from .models import Regions, GorRayon, Nsp, Otrasl, PodOtrasl, Org, orgContact, Sheff, CatUslugi, VidUslugi, Uslugi


class RegionsAdmin(admin.ModelAdmin):
	#inlines = (NspInline,)
	list_display = ('id', 'name')
	#list_display_links = ('name')


class GorRayonAdmin(admin.ModelAdmin):
	list_display = ('id', 'region', 'name')
	list_filter = ('region',)
	list_per_page = 10


class NspAdmin(admin.ModelAdmin):
	list_display = ('region', 'rayon', 'name', 'mo')
	list_filter = ('region', 'rayon', 'mo',)

class OrgAdmin(admin.ModelAdmin):
	list_display = ('inn', 'name', 'otrasl', 'pod_otrasl', 'nsp', 'okved')
	list_filter = ('region', 'rayon', 'otrasl',)
	search_fields = ('name', 'sheff__fm')

class OtraslAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


class PodOtraslAdmin(admin.ModelAdmin):
	list_display = ('id', 'otrasl', 'name')
	list_filter = ('otrasl',)

class orgContactAdmin(admin.ModelAdmin):
	list_display = ('org', 'adres', 'telefone', 'email', 'url')
	list_filter = ('org__rayon','org__otrasl',)

class SheffAdmin(admin.ModelAdmin):
	list_display = ('org', 'fm', 'im', 'ot', 'inn_ruk',  'active')
	search_fields = ('org__name_short', 'fm', 'im', 'ot')
	list_filter = ('org__rayon','org__otrasl',)
	# Related Field has invalid lookup: icontains
	# https://code.djangoproject.com/ticket/2331
	#list_filter = ('org',)
class CatUslugiAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class VidUslugiAdmin(admin.ModelAdmin):
	list_display = ('id', 'cat_usl', 'name', 'pod_otr_txt')

class UslugiAdmin(admin.ModelAdmin):
	list_display = ('id', 'cat_usl', 'vid_uslugi', 'description', 'documents', 'price', 'url_gosuslugi')

#class OtraslAdmin(admin.ModelAdmin):
#	list_display = ('name')


#admin.site.register(Regions)
admin.site.register(Regions, RegionsAdmin)
#admin.site.register(GorRayon)
admin.site.register(GorRayon, GorRayonAdmin)
admin.site.register(Nsp, NspAdmin)
#admin.site.register(Nsp)
admin.site.register(Otrasl, OtraslAdmin)
admin.site.register(PodOtrasl, PodOtraslAdmin)
admin.site.register(Org, OrgAdmin)
admin.site.register(orgContact, orgContactAdmin)
admin.site.register(Sheff, SheffAdmin)
admin.site.register(CatUslugi, CatUslugiAdmin)
admin.site.register(VidUslugi, VidUslugiAdmin)
admin.site.register(Uslugi, UslugiAdmin)
