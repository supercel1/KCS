from django.db import models
from datetime import timezone

class Room(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    is_private = models.BooleanField(default=True)
    created_at = DatetimeField(default=timezone.now())

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
