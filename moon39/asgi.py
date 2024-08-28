"""
ASGI config for moon39 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter 
# # from  moon39. routings import websocket_urlpatterns  
# from . import routing
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

# from  routing import websocket_urlpatterns


import app1.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moon39.settings")

# django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            app1.routing.websocket_urlpatterns
        )
    ),
}) 