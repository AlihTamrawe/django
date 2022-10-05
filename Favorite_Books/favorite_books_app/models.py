import imp
from operator import mod
from pydoc import describe
from django.db import models
from login_app.models import *
from tkinter import CASCADE


class BookManager(models.Manager):
    def validate_Book(self,postdata):
        date_format = "%Y-%m-%d"  # %Y for year, %m for month and %d for day
        errors = {}
        
        if len(postdata['title']) < 5 :
            errors["title"] = "Title should be at least 8 number"
        # Book.objects.filter()
        print(postdata.get('title'))
        if len(Book.objects.filter(title=postdata.get('title')))>1 :
            errors["title"] = "The Title is Already Exists"

        if len(postdata['description']) < 10:
            errors["description"] = "description should be at least 8 number"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,default="none")
    added_on = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now=True)
    uploadeder = models.ForeignKey(User ,related_name="uploader",on_delete=CASCADE)
    liker = models.ManyToManyField(User, related_name="favor")
    objects = BookManager()
