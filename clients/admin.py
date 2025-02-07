from django.contrib import admin
from .models import Client, Job, Messages

# Register your models here.
admin.site.register(Client)
admin.site.register(Job)
admin.site.register(Messages)
