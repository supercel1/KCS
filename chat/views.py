from django.shortcuts import render, redirect

def index(request):
    return render(request, 'chat/index.html', {})

def home(request):
    return render(request, "chat/home.html")

def chat_room(request):
    room, created = Room.objects.get_or_create(name=name)
    messages = reversed(room.objects.order_by('created_at')[:100])
    context = {
        'room': room,
        'messages': messages
    }

    return render(request, "chat/chatroom.html", context)

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
    