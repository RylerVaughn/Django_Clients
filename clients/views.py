from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Job

def index(request):
    return render(request, 'clients/index.html')

def clientel(request):
    return render(request, 'clients/clientel.html', {'client_list': Client.objects.all()})

def jobs(request):
    return render(request, 'clients/jobs.html', {'jobs_list': Job.objects.all()})

def create(request):
    return render(request, 'clients/create.html')