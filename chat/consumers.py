from channels import Group
from channels.sessions import channel_session
from .models import Room
import json

@channel_session
def ws_connect(message):
    prefix, label = message['path'].strip('/').split('/')
    room = Room.objects.get(label=label)
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = room.label

@channel_session
def ws_disconnect(close_code):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    Group('chat-'+label, channel_layer=message.channel_layer).discard(message.reply_channel)

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)

    text = json.loads(message['text'])
    m = room.messages.create(**data)
    Group('chat-'+label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})
