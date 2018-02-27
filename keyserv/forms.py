from django import forms
from keyserv.models import User, Message

class KeyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'pub_key']


class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ['to_user', 'text']
