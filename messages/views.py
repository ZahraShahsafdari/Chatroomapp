from django.shortcuts import render
from djnago.models import Users
from django.http import HttpResponse
from users.models import Messages

# Create your views here.
def add_message(request):
    m = Messages (
        text = request.POST['text'],
        sender = 1,
        receiver = request.POST['receiver']
    )
    m.save()
    return HttpResponse("Message saved!")

def chat(request, user_id = None):
    print('user_id', user_id)
    return render(
        request,
        'chat.html',
        context={
            'users': Users.objects.all(),
            'receiver': user_id
        }
    )