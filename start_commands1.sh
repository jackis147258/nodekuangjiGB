#!/bin/bash      
nohup daphne -b 0.0.0.0 -p 8003 moon39.asgi:application &
nohup celery -A moon39 worker --loglevel=info --settings=moon39.settings &
nohup celery -A moon39 beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &

