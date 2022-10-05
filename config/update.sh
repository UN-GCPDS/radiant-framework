#!/usr/bin/bash

sudo rm -R dimawebapp.old/
mv dimawebapp/ dimawebapp.old/
wget -c https://github.com/UN-Dima/dimawebapp/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
mv dimawebapp-main/ dimawebapp/

. ./venv39/bin/activate
cd dimawebapp
sudo chown -R www:www db
python manage.py collectstatic
python manage.py makemigrations && python manage.py migrate && python manage.py migrate --database=dima_database
cd ..

sudo chown -R `whoami` /www/
sudo service apache24 restart
