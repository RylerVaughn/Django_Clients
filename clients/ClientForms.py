from django import forms
from .models import Client, Job

class client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'details']

class job_form(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['date', 'price', 'client']

