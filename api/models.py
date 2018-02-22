from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField()

class Content(models.Model):
    name = models.TextField()
    author = models.ForeignKey(User, related_name='content')
