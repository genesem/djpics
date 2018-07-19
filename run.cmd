@echo off
set PORT=8000
cd .\djapp
start python manage.py runserver %PORT%
echo openning localhost:%PORT% in browser..
python -m webbrowser -t "http://localhost:%PORT%"

