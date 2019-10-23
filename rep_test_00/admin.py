from django.contrib import admin

# Register your models here.

from .models import Regions, GorRayon, Nsp

'''
class NspInline(admin.StackedInline):
	model = Nsp
	fk_name = 'region'


class RegionsAdmin(admin.ModelAdmin):
	inlines = (NspInline,)
	#list_display = ('name')
	#list_display_links = ('name')
'''


#class GorRayonAdmin(admin.ModelAdmin):
	#inlines = [NspInline]
	#list_display = ('region', 'name')
	#list_display_links = ('region', 'name')


#class NspAdmin(admin.ModelAdmin):
	#inlines = [RegionInline,]
	#list_display = ('region', 'rayon', 'name')



admin.site.register(Regions)	
#admin.site.register(Regions, RegionsAdmin)	
admin.site.register(GorRayon)
#admin.site.register(GorRayon, GorRayonAdmin)
#admin.site.register(Nsp, NspAdmin)
admin.site.register(Nsp)

