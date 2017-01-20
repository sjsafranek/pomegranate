#!/bin/bash

# create file for logs
if [ ! -d "`pwd`/log" ]; then
	mkdir log
fi

# create app config 
if [ ! -f "`pwd`/config.json" ]; then
    echo '{"default":{"ENGINE":"django.contrib.gis.db.backends.spatialite","NAME":"geo.sqlite3","OPTIONS":{"timeout": 20}}}' >> config.json  
fi

# setup db and check for changes
python3 manage.py makemigrations
python3 manage.py migrate

# create admin user
if [ ! -f "`pwd`/credentials.ini" ]; then
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@pomegranate.com', 'dev')" | python3 manage.py shell
	echo "[credentials]\nusername:admin\npassword:dev\n" >> credentials.ini
fi

