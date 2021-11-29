#!/bin/bash
# django-run.sh
sleep 10
python manage.py migrate && python manage.py runserver 0.0.0.0:8080