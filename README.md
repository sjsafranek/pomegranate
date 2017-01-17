# Pomegranate


## Quick Start

### Install requirements::
	$ sudo pip3 install django
	$ sudo pip3 install jinja2

* requires django 1.9 =<

### Setup database::
	$ python3 manage.py migrate
	$ python3 manage.py makemigrations

### Create superuser::
	$ python3 manage.py createsuperuser

### Launch server::
	$ python3 manage.py runserver
	$ python3 manage.py runserver 0.0.0.0:8000

### Setup Users
	- http://localhost:8000/admin/
	- login with superuser
	- http://localhost:8000/admin/auth/group/
	- add users


### Vagrant
	$ vagrant init
	$ vagrant up
vagrant box add https://atlas.hashicorp.com/debian/boxes/jessie64/ --provider virtualbox
sudo journalctl -f -u pomegranate.service
