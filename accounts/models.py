from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.base_model import BaseModel



class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=40, blank=False, null=False)


    USERNAME_FIELD = "username"
    
    def __str__(self) -> str:
        return self.email



