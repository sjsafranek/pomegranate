#!/bin/bash

if [ -f "`pwd`/credentials.ini" ]; then
	exit 1
fi

if [ ! -f "`pwd`/config.json" ]; then
    echo '{"default":{"ENGINE":"django.contrib.gis.db.backends.spatialite","NAME":"geo.sqlite3","OPTIONS":{"timeout": 20}}}' >> config.json  
fi

if [ ! -d "`pwd`/log" ]; then
	mkdir log
fi

# setup db
python3 manage.py makemigrations
python3 manage.py migrate

# create admin user
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@pomegranate.com', 'dev')" | python3 manage.py shell
echo "[credentials]\nusername:admin\npassword:dev\n" >> credentials.ini
