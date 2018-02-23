from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User, Message
# Create your views here.

def index(request):
    return render(request, "keyserv/index.html")

def messages(request):
    messages = Message.objects.order_by('-post_date')

    return render(request, "keyserv/messages.html", {'messages': messages})

def keys(request):
    keys = User.objects.order_by('-id')
    
    return render(request, "keyserv/keys.html", { 'keys': keys })

def key_deets(request, key_id):
    key = get_object_or_404(User, pk=key_id)

    return render(request, 'keyserv/key.html', { 'key': key })

def key_upload(request):

    return render(request, 'keyserv/key_upload.html')

def message_deets(request, mess_id):
    message = get_object_or_404(Message, pk=mess_id)

    return render(request, 'keyserv/message.html', { 'message': message })

