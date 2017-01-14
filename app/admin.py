#from django.contrib import admin
from django.contrib.gis import admin

# Register your models here.
from .models import Zone
from .models import Furniture

#admin.site.register(Zone, admin.ModelAdmin)
#admin.site.register(Furniture, admin.ModelAdmin)
admin.site.register(Zone, admin.GeoModelAdmin)
admin.site.register(Furniture, admin.GeoModelAdmin)
