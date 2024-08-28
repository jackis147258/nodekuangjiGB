#!/bin/bash      
nohup daphne -b 0.0.0.0 -p 9003 moon39.asgi:application > /www/wwwroot/nodekuangjiGB/nohubdaphne.log 2>&1 &
nohup celery -A moon39 worker --loglevel=info > /www/wwwroot/nodekuangjiGB/celerymoon39.log 2>&1 &
nohup celery -A moon39 beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler > /www/wwwroot/nodekuangjiGB/celerymoon39beat.log 2>&1 &

