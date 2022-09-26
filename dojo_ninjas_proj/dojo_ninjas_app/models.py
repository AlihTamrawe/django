from operator import mod
from unicodedata import name
from django.db import models


class Dojos(models.Model):
    name = models.TextField(max_length=255)
    city = models.TextField(max_length=255)
    state = models.TextField(max_length=2)

class Ninjas(models.Model):
    first_name = models.TextField(max_length=255)
    last_ame = models.TextField(max_length=255)
    Dojo = models.ForeignKey(Dojos, related_name="ninja", on_delete = models.CASCADE)



# Create your models here.
