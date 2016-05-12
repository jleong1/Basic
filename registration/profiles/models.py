from __future__ import unicode_literals
from django.db import models

class Profiles(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
