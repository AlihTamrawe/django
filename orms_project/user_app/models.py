from platform import release
from turtle import update
from django.db import models


class Movie(models.Model):
        title = models.TextField(max_length=45)
        description = models.TextField()
        release_date  = models.DateTimeField()
        duration = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)




class Users(models.Model):
        first_name = models.TextField(max_length=45)
        last_name= models.TextField(max_length=45)
        email_address  = models.EmailField()
        age = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        def __str__(self):
                return f"<Users object: {self.first_name} ({self.last_name})>"



