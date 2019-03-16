from django.shortcuts import render, redirect
from .models  import Room

class RoomView():
    def home(request):
        return render(request, "chat/chatroom.html")
    
    def chat_room(request):
        room, created = Room.objects.get_or_create(name=name)
        messages = reversed(room.objects.order_by('created_at')[:100])
        context = {
            'room': room,
            'messages': messages
        }
    
        return render(request, "chat/chatroom.html", context)
