"""
ASGI config for websocket_auth project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_auth.settings')
django_asgi_application = get_asgi_application()

from websocket_auth.chat_config import routing
from websocket_auth.chat_config.jwt_middleware import JWTAuthMiddleware 



application = ProtocolTypeRouter(
    {
        'http': django_asgi_application,
        'websocket': 
        JWTAuthMiddleware(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    }
)