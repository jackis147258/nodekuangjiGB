# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'room/', consumers.ChatConsumer.as_asgi()),
    # re_path(r'log/logs/', consumers.LogConsumer.as_asgi()),
]