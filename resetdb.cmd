@echo off

cd .\djapp
echo Reset migrations..
rm -rf main/migrations/*
rm db.sqlite3
rm -rf www/media/*

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email t@test.com

python manage.py makemigrations main
python manage.py migrate main

