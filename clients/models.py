from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    details = models.TextField()
    contact = models.CharField(max_length=15, default='NaN')

    def __str__(self):
        return f'{self.name}, address: {self.address}, details: {self.details}'

class Job(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Messages(models.Model):
    message = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

