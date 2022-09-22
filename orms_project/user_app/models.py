from platform import release
from turtle import update
from django.db import models

class movie(models.Model):
    title = models.TextField(max_length=45)
    description = models.TextField()
    release_date  = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



