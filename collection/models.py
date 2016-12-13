from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    urllink = models.CharField(max_length=3000, null=True)
    slug = models.SlugField(unique=True)
    

