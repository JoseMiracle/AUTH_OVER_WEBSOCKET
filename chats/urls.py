from django.urls import path
from chats.views import GetOrGenerateWebSocketIDAPIView


urlpatterns = [
    path('get-or-generate-chat-id/', GetOrGenerateWebSocketIDAPIView.as_view(), name='get_or_generate_chat_id'),
    
]