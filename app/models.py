from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = User()
    name = ''
    description = ''
    completed = False
    created = 
