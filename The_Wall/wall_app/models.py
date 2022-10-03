from cgitb import text
from distutils.text_file import TextFile
from email import message
from tkinter import CASCADE
from tkinter.tix import Tree
from turtle import title, update
from django.db import models
from login_app.models import User

class Messages(models.Model):
    message = models.TextField(max_length=255)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)
    poster = models.ForeignKey(User ,related_name="messager",on_delete=CASCADE)
    

class Comments(models.Model):
    comment = models.TextField(max_length=255)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)
    commander = models.ForeignKey(User ,related_name="commander",on_delete=CASCADE)
    reply = models.ForeignKey(Messages ,related_name="reply",on_delete=CASCADE)
