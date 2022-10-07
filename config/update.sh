#!/usr/bin/bash

sudo rm -R dimawebapp.old/
mv dimawebapp/ dimawebapp.old/
wget -c https://github.com/UN-Dima/dimawebapp/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
mv dimawebapp-main/ dimawebapp/

. ./venv39/bin/activate
cd dimawebapp
sudo chown -R $USER db
python manage.py collectstatic --noinput
python manage.py makemigrations && python manage.py migrate && python manage.py migrate --database=dima_database
python manage.py createsuperuser --username yeison --email yencardonaal@unal.edu.co
cd ..

sudo chown -R $USER /www/
sudo chown -R www:www /www/dimawebapp/db
sudo service apache24 restart
