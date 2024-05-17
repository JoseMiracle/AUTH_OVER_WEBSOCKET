from django.db import models
from django.contrib.auth import get_user_model
from utils.base_model import BaseModel

User = get_user_model()



class WebSocketChatID(BaseModel):
    user = models.ForeignKey(User, related_name='chat_user', on_delete=models.CASCADE)
    other_user = models.ForeignKey(User, related_name='chat_other_user', on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat between {self.user.username} and {self.other_user.username}"

class Message(BaseModel):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()