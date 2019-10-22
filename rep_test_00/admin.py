from django.contrib import admin

# Register your models here.

from .models import Regions, GorRayon, Nsp
'''
class RegionsAdmin(admin.ModelAdmin):
	list_display = ('name')
	#list_display_links = ('name')
'''
class GorRayonAdmin(admin.ModelAdmin):
	list_display = ('region', 'name')
	#list_display_links = ('region', 'name')

class NspAdmin(admin.ModelAdmin):
	list_display = ('region', 'rayon', 'name')


admin.site.register(Regions)	
#admin.site.register(Regions, RegionsAdmin)	
#admin.site.register(GorRayon)
admin.site.register(GorRayon, GorRayonAdmin)
admin.site.register(Nsp, NspAdmin)

