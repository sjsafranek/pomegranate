# Pomegranate


## Quick Start

### Install Spatialite
#### Linux
	sudo apt-get install spatialite-bin
#### Windows
	Download http://www.gaia-gis.it/gaia-sins/windows-bin-amd64/mod_spatialite-4.3.0a-win-amd64.7z
	Put into Path
	Test: `python3 test_spatialite.py`

### Install Requirements (Linux)
#### Get requirements::
	$ aptitude -yy install install libgeos++ binutils libproj-dev gdal-bin python3-pip python3-gdal python3-jinja2 python3-django 

### Install Requirements (Windows)
#### Get requirements::
	pip3 install django
	pip3 install jinja2
	pip3 install pyspatialite
	pip3 install GDAL
	pip3 install sqlite3

### Setup database::
	$ python3 manage.py makemigrations
	$ python3 manage.py migrate

### Create superuser::
	Use auto generated admin user::
		- username: admin
		- password: dev
	
	Create new admin user::
		$ python3 manage.py createsuperuser

### Launch server::
	$ python3 manage.py runserver 0.0.0.0:8000

### Setup Users
	- http://localhost:8000/admin/
	- login with superuser
	- http://localhost:8000/admin/auth/group/
	- add users


### Vagrant
	$ vagrant up
	visit http://172.20.0.10:8080/
	visit localhost:8080/


vagrant box add https://atlas.hashicorp.com/debian/boxes/jessie64/ --provider virtualbox
sudo systemctl status pomegranate.service
sudo journalctl -f -u pomegranate.service

