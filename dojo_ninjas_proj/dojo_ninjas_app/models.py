from django.db import models


class Dojos(models.Model):
    name = models.TextField(max_length=255)
    city = models.TextField(max_length=255)
    state = models.TextField(max_length=2)
    desc = models.TextField(default="old dojo")

class NinjaManager(models.Manager):
    def validate_ninja(request,formData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(formData['name_from']) < 5:
            errors["name_from"] = "Blog name should be at least 5 characters"
        if len(formData['desc_from']) < 10:
            errors["desc_from"] = "Blog description should be at least 10 characters"
        if str(formData['name_from']).isalpha():
            errors["name_from"]="the name Need to be Alpha "
        return errors

class Ninjas(models.Model):
    first_name = models.TextField(max_length=255)
    last_ame = models.TextField(max_length=255)
    Dojo = models.ForeignKey(Dojos, related_name="ninja", on_delete = models.CASCADE)
    objects = NinjaManager()



# Create your models here.
