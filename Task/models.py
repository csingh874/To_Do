from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class user_Task(models.Model):
    author = models.CharField(max_length=50,null=True, blank=True)
    title = models.CharField(max_length=50)
    descreption = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title