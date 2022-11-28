from mailbox import Message

from django.shortcuts import render, redirect, HttpResponse
from .models import Room, Notepad


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():  # if the room name that was inputed exists
        return redirect('/' + room + '/?username=' + username)  # we redirect to the room
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)  # we redirect to the room


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=Message, user=username, room=room_id
    )
    new_message.save()
# return HttpResponse('Message Sent Successfully!')
