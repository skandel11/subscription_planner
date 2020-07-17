from django.db import models
from datetime import datetime

class Subscription(models.Model):
    service=models.CharField(max_length=20)
    email=models.EmailField(max_length=50, blank=True)
    personal_email=models.EmailField(max_length=50, blank=True)
    username=models.CharField(max_length=20, blank=True)
    category=models.CharField(max_length=20, blank=True)
    price=models.IntegerField()
    subscribe_date=models.DateField(default=datetime.now)
    expiry_date= models.DateField(default=datetime.now)
    is_published=models.BooleanField(default=True)
    def __str__(self):
        return self.service
    