#!/usr/bin/bash

sudo rm -R dimawebapp.old/
mv dimawebapp/ dimawebapp.old/
wget -c https://github.com/UN-Dima/dimawebapp/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
mv dimawebapp-main/ dimawebapp/

. ./venv39/bin/activate
cd dimawebapp
python manage.py collectstatic
cd ..

sudo chown -R `whoami` /www/
sudo service apache24 restart