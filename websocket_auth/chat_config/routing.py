from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
     re_path(r'ws/chat/(?P<chat_id>[0-9a-fA-F-]{36})/$', consumers.DirectMessageConsumer.as_asgi()),
]