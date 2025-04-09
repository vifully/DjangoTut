from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'HELLO new here!'},
    {'id': 2, 'name': 'design w / me '},
    {'id': 3, 'name': 'devs yo'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id']== int(pk):
            room = i
    context = {'room': room}    
    return render(request, "base/room.html", context)
