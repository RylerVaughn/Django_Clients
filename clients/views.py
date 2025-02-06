from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Job
from .ClientForms import client_form, job_form

def index(request):
    return render(request, 'clients/index.html')

def clientel(request):
    return render(request, 'clients/clientel.html', {'client_list': Client.objects.all()})

def jobs(request):
    return render(request, 'clients/jobs.html', {'jobs_list': Job.objects.all()})

def create(request):
    if request.method == 'POST':
        form = client_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('clients:index')
    else:
        form = client_form()
    return render(request, 'clients/cform.html/', {'form': form})

def ajob(request):
    if request.method == 'POST':
        form = job_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('clients:index')
    else:
        form = job_form()
        return render(request, 'clients/jform.html/', {'form': form})