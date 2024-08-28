#!/bin/bash      
nohup celery -A moon39 worker --loglevel=info > /www/wwwroot/djangotokens/celerymoon39.log 2>&1 &
nohup celery -A moon39 beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler > /www/wwwroot/djangotokens/celerymoon39beat.log 2>&1 &
