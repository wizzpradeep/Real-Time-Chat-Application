from django import forms
from .models import *
from django.core.exceptions import ValidationError


class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields  = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if Rooms.objects.filter(name=name).exists():
            raise ValidationError("Room already exist.")
        if len(name) <5 :
            raise ValidationError("Room name must constain at least 5 chars.")
        
        return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields  = ['content']