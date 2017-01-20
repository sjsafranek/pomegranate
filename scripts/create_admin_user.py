#!/usr/bin/python

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
    pass



'''
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@pomegranate.com', 'dev')" | python3 manage.py shell

'''