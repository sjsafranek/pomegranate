#!/bin/bash
# sudo -i -u postgres
# sudo apt-get install -y postgresql postgresql-contrib
sudo -u postgres psql -c "CREATE USER pomegranateuser WITH PASSWORD 'dev'"
sudo -u postgres psql -c "CREATE DATABASE pomegranatedb"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE pomegranatedb TO pomegranateuser"
sudo -u postgres psql -c "ALTER USER pomegranateuser WITH SUPERUSER;"
sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology; CREATE EXTENSION fuzzystrmatch; CREATE EXTENSION postgis_tiger_geocoder;" pomegranatedb
# sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology; CREATE EXTENSION postgis_sfcgal; CREATE EXTENSION fuzzystrmatch; CREATE EXTENSION address_standardizer; CREATE EXTENSION address_standardizer_data_us; CREATE EXTENSION postgis_tiger_geocoder;" pomegranatedb
