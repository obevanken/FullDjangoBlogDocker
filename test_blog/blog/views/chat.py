from django.views.generic import View
from django.shortcuts import render
from ..models import Room
from django.utils.safestring import mark_safe
import json


class ChatView(View):
    template_name = "chat.html"

    def get(self, request, room_name, **kwargs):
        room = Room.objects.filter(title=room_name).first()
        if not room:
            room = Room.objects.create(title=room_name)
            room.user.add(request.user)
            room.save()
            return render(request, self.template_name, {'room_name_json': mark_safe(json.dumps(room_name))})
        else:
            room.user.add(request.user)
            room.save()
            print(room.messages)
            return render(request, self.template_name, {'room_name_json': mark_safe(json.dumps(room_name)),
                                                        'messages': room.messages.all().order_by('created_at')})


class MyChat(View):
    template_name = "my_chat.html"

    def get(self, request, pk, **kwargs):
        my_rooms = Room.objects.filter(title=pk)
        rooms = Room.objects.filter(user=request.user)
        return render(request, self.template_name, {'my_rooms': my_rooms,
                                                    'rooms': rooms})
