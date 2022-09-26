from turtle import title
from django.db import models

class Books(models.Model):
    title = models.TextField(max_length=255)
    desc = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


class Authors(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Books, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)