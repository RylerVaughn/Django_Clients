from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.index, name='index'),
    path('clientel/', views.clientel, name='clientel'),
    path('jobs/', views.jobs, name='jobs'),
    path('create/', views.create, name='create'),
    path('ajob/', views.ajob, name='ajob')
]