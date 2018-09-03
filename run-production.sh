#!/bin/sh

# core_count: cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l
# workers   : (2 x core_count) + 1
python manage.py makemigrations && \
python manage.py migrate && \
exec gunicorn deployment.wsgi:application --bind 0.0.0.0:8000 --workers 3