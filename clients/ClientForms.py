from django import forms
from .models import Client, Job, Messages

class client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'details', 'contact']

class job_form(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['date', 'price', 'client']

class Message_Form(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message', 'client']

