#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn GalleryStoreBackend.wsgi:application --bind 0.0.0.0:8000
