from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from .models import Rooms, Message
from channels.db import database_sync_to_async


class MyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Get the room name and group name
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_name}"

        # Add the user to the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the incoming message
        text_data_json = json.loads(text_data)
        
        message = text_data_json['message']
        username = text_data_json['username']
        room_id = text_data_json['room_id']

        # Fetch the room and user from the database asynchronously
        room = await database_sync_to_async(Rooms.objects.get)(id=room_id)
        user = await database_sync_to_async(User.objects.get)(username=username)

        # Create the new message object and save it to the database
        message_obj = await database_sync_to_async(Message.objects.create)(
            user=user, room=room, content=message
        )

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_obj.content,
                'username': message_obj.user.username,
                'room_id': room_id,
            }
        )

    async def chat_message(self, event):
        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'room_id': event['room_id'],
        }))


