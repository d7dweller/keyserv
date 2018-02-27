from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import KeyForm, MessageForm
from .models import User, Message
# Create your views here.

def index(request):
    return render(request, "keyserv/index.html")

def messages(request):
    messages = Message.objects.order_by('-post_date')

    return render(request, "keyserv/messages.html", {'messages': messages})

def keys(request):
    keys = User.objects.order_by('-id')
    
    return render(request, "keyserv/keys.html", {'keys': keys})

def key_deets(request, key_id):
    key = get_object_or_404(User, pk=key_id)

    return render(request, 'keyserv/key.html', {'key': key})

def key_upload(request):
    if request.method == 'POST':
        form = KeyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/keys/')
    else:
        form = KeyForm()
    return render(request, 'keyserv/key_upload.html', {'form': form})

def message_deets(request, mess_id):
    message = get_object_or_404(Message, pk=mess_id)

    return render(request, 'keyserv/message.html', { 'message': message })

def message_upload(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/messages/')
    else:
        form = MessageForm()
    return render(request, 'keyserv/message_upload.html', {'form': form})

