from django.db import models

class Shows(models.Model):
    title = models.TextField(max_length=255)
    network = models.TextField(max_length=255)
    release_date = models.DateTimeField(auto_now=True)
    desc = models.TextField(default="none")