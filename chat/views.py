from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import RoomsForm, MessageForm
from .models import Rooms, Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from chat.decorators import login_required
from django.utils.decorators import method_decorator


class RoomsView(View):
    # @method_decorator(login_required)
    def get(self, request):

        rooms = Rooms.objects.all() 
        form = RoomsForm()

        context = {
            'form': form,
            'rooms':rooms,
        }
        return render(request, 'rooms.html', context)
    # @method_decorator(login_required)
    def post(self, request):

        if Rooms.objects.filter(user=request.user).exists():
            return redirect('myroom', room_id=request.user.rooms.id) 


        rooms = Rooms.objects.all()

        form = RoomsForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user  
            room.save()
            return redirect('rooms')  
        
        context = {
            'form': form,
            'rooms':rooms,
        }
        return render(request, 'rooms.html', context)



class RoomView(View):

    def get(self, request, room_id):
        
        room = get_object_or_404(Rooms, id=room_id)
        messages = room.message.all().order_by('created_at')  

        form = MessageForm()

        context = {
            'room': room,
            'chats': messages,
            'form': form,
        }
        return render(request, 'room.html', context)

    def post(self, request, room_id):

        room = get_object_or_404(Rooms, id=room_id)
        messages = room.message.all().order_by('created_at')
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user 
            message.room = room  
            message.save()

        context = {
            'room': room,
            'messages': messages,
            'form': form,
        }
        return render(request, 'room.html', context)



def delete_room(request, room_id):
    room = get_object_or_404(Rooms, id=room_id).delete()
    return redirect('rooms')

