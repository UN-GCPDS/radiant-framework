#!/usr/bin/bash

#rm db/db.sqlite3
#rm db/fixed.sqlite3

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

python manage.py makemigrations
python manage.py migrate --database=dima_database
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser --username yeison --email yencardonaal@unal.edu.co
