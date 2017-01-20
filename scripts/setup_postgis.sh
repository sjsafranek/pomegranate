#!/bin/bash
# sudo -i -u postgres
psql -c "CREATE USER geodjango WITH PASSWORD 'dev'"
psql -c "CREATE DATABASE geodjangodb"
psql -c "GRANT ALL PRIVILEGES ON DATABASE geodjangodb TO geodjango"
psql -c "ALTER ROLE geodjango SUPERUSER;"

# psql -U geodjango -d geodjangodb -h localhost
# CREATE EXTENSION postgis;

