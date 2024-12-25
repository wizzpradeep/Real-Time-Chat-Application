from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rooms(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} >> {self.user.username}"

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='message')
    content  = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} >> {self.room.name} >> {self.user.username}"