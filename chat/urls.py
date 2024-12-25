from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/', RoomsView.as_view(), name='rooms'),
    path('room/<int:room_id>/', RoomView.as_view(), name='myroom'),
    path('delete-room/<int:room_id>/', delete_room, name='delete_room'),
]
