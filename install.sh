#!/bin/sh
sudo apt install python3-dev libpq-dev -y
pip install -r requirements.txt
python3 manage.py migrate
export DJANGO_SUPERUSER_PASSWORD=cloud
export DJANGO_SUPERUSER_USERNAME=cloud
export DJANGO_SUPERUSER_EMAIL=cloud@a.com
python3 manage.py createsuperuser --noinput
echo '@reboot /home/ubuntu/tasks/run.sh' | crontab