import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chats.models import Message
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async


class DirectMessageConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_room_name = f'chat_{self.id}'

        await self.accept()

        if self.is_error_exists():
            error = {
                'error': str(self.scope['error'])
            }
            await self.send(text_data=json.dumps(error))
            await self.close()

        else:            
            await self.channel_layer.group_add(    
                self.chat_room_name,
                self.channel_name
            )
        
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_room_name, self.channel_name
        )
    
    # Receive message from WebSocket
    async def receive(self, text_data):
        if self.scope.get('user_id') is not None:
            
            sender_id = self.scope.get('user_id')
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            receiver_id = text_data_json['receiver_id']

            message = await database_sync_to_async(Message.objects.create)(
                sender_id=sender_id,
                receiver_id=receiver_id,  
                message=message
            )    

            await self.channel_layer.group_send(
                self.chat_room_name,
            {
                'type': 'chat_message',
                'message_info': await self.message_information(message),
                }
            )
        
    async def chat_message(self, event):   
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def message_information(self, message):
        return {
            "message": message.message,
            "sender": message.sender.username       
            }


    

    def is_error_exists(self):
        """This checks if error exists during websockets"""

        return True if 'error' in self.scope else False
               
