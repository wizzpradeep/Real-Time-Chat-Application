from django.contrib import admin
from .models import *

# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    list_display = ['user','name','created_at']
    list_filter = ['user','name','created_at']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['content','room',  'user','created_at']
    list_filter = ['room',  'user','created_at']
    list_per_page = 100


admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Message, MessageAdmin)