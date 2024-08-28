#!/bin/bash
kill -9 $(pgrep -f "celery -A moon39 worker")
kill -9 $(pgrep -f "celery -A moon39 beat")
kill -9 $(pgrep -f "daphne -b 0.0.0.0 -p 9003 moon39.asgi:application")
