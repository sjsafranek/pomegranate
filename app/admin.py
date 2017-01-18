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


#conf.py
#import builtins
#
# Creates an Admin user on startup
from django.contrib.auth.models import User
try:
    username = "admin"
    email = "admin@pomegranate.com"
    password = "dev"
    User.objects.create_superuser(username, email, password)
    print("\n")
    print("Admin user created:")
    print("*** username: ", username)
    print("*** password: ", password)
    print("\n")
except Exception as e:
    #print(e)
    pass



'''
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@pomegranate.com', 'dev')" | python3 manage.py shell

'''
