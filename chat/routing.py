from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path(r'ws/<int:room_id>/', MyConsumer.as_asgi()),

]