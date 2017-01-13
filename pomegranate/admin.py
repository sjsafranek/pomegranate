from django.contrib import admin

# Register your models here.
from .models import Zone
from .models import Furniture

admin.site.register(Zone)
admin.site.register(Furniture)
