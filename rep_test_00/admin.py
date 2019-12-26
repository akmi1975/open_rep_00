from django.contrib import admin

# Register your models here.

from .models import Regions, GorRayon, Nsp, Otrasl, PodOtrasl, Org


class RegionsAdmin(admin.ModelAdmin):
	#inlines = (NspInline,)
	list_display = ('id', 'name')
	#list_display_links = ('name')


class GorRayonAdmin(admin.ModelAdmin):
	list_display = ('region', 'name')
	list_filter = ('region',)
	list_per_page = 10


class NspAdmin(admin.ModelAdmin):
	list_display = ('region', 'rayon', 'name', 'mo')
	list_filter = ('region', 'rayon', 'mo',)

class OrgAdmin(admin.ModelAdmin):
	list_display = ('inn', 'name', 'otrasl', 'pod_otrasl', 'nsp', 'okved')
	list_filter = ('region', 'rayon', 'nsp', 'otrasl', 'pod_otrasl',)

class OtraslAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


class PodOtraslAdmin(admin.ModelAdmin):
	list_display = ('id', 'otrasl', 'name')
	list_filter = ('otrasl',)

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

