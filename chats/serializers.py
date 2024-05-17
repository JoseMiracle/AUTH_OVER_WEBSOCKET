from rest_framework import serializers
from chats.models import WebSocketChatID
from django.db.models import Q


class WebSocketChatIDSerializer(serializers.Serializer):
    web_socket_chat_id = serializers.ReadOnlyField()
    other_user_id = serializers.UUIDField(write_only=True)


    def create(self, validated_data):

        condition_1 = Q(user=validated_data["other_user_id"], other_user=self.context['request'].user.id)
        condition_2 = Q(other_user=validated_data["other_user_id"], user=self.context['request'].user.id)

        web_socket_chat_obj = WebSocketChatID.objects.filter(
            condition_1 | condition_2
        ).first()

        web_socket_chat_id = None
        
        if web_socket_chat_obj is None:
            web_socket_chat_obj = WebSocketChatID.objects.create(
                                            user_id=self.context['request'].user.id, 
                                            other_user_id=validated_data['other_user_id']
                                            )
            web_socket_chat_id = web_socket_chat_obj.id
        
        else:
            web_socket_chat_id = web_socket_chat_obj.id
        
            
        return {
            "web_socket_chat_id": web_socket_chat_id 
        }
    


            
