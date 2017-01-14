#from django.contrib import admin
from django.contrib.gis import admin

# Register your models here.
from .models import Zone
from .models import Furniture
from .models import Person
from .models import Room

#admin.site.register(Zone, admin.ModelAdmin)
admin.site.register(Zone, admin.GeoModelAdmin)
admin.site.register(Furniture, admin.GeoModelAdmin)
admin.site.register(Person, admin.GeoModelAdmin)
admin.site.register(Room, admin.GeoModelAdmin)
