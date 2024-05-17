from chats.serializers import WebSocketChatIDSerializer
from rest_framework import generics, permissions


class GetOrGenerateWebSocketIDAPIView(generics.CreateAPIView):
    
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = WebSocketChatIDSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
