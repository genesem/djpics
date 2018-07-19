@echo off

cd .\djapp
echo Reset migrations..
rm -rf main/migrations/*

python manage.py makemigrations main
python manage.py migrate main

