#!/bin/sh

# database migrations
python manage.py migrate 

# create superuser
python manage.py createadmin

# Start Gunicorn processes
echo Starting Gunicorn...
exec gunicorn hardboiledegg.wsgi:application \
    --bind "0.0.0.0:8000" \
    --workers 3 \
    --timeout 300 \
    
    