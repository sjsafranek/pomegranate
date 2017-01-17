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
	Use auto generated admin user::
		- username: admin
		- password: dev
	
	Create new admin user::
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
	visit http://172.20.0.10:8080/


vagrant box add https://atlas.hashicorp.com/debian/boxes/jessie64/ --provider virtualbox
sudo systemctl status pomegranate.service
sudo journalctl -f -u pomegranate.service

