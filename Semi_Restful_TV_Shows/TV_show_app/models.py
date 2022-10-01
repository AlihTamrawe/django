from django.db import models
import re
import datetime
from django.utils import timezone,dates
class ShowsManager(models.Manager):
    def validate_show(request,formData):
        date_format = "%Y-%m-%d"  # %Y for year, %m for month and %d for day
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(formData['title_from']) < 2:
            errors['title_from'] = "Title name should be at least 2 characters"
        if len(formData['network_from']) < 3:
            errors["network_from"] = "Network should be at least 3 characters"
        if len(formData['desc_from']) < 10:
            errors["desc_from"] = "description should be at least 10 characters"
        if datetime.datetime.today() < datetime.datetime.strptime(formData['date_from'],date_format) :
            errors['date_from'] = "Date is not accurate and must be in the past"
        return errors
    def basic_validator(self, postData):    
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors


class Shows(models.Model):
    title = models.TextField(max_length=255)
    network = models.TextField(max_length=255)
    release_date = models.DateTimeField(default=datetime.date.today())
    desc = models.TextField(default="none")
    update_time =  models.DateTimeField(auto_now=True)
    objects = ShowsManager()
def insert2(p):
        titles = p.get('title_from')
        networks =  p.get('network_from')
        date = p.get('date_from')
        desc = p.get('desc_from')
        Shows.objects.create(title=titles,network=networks,release_date=date,desc=desc)
        last = Shows.objects.last()
        return last.id
def update2(p,c):
    titles = p.get('title_from')
    networks =  p.get('network_from')
    date = p.get('date_from')
    desc = p.get('desc_from')
    c.title=titles
    c.network=networks
    c.update_time=timezone.now()
    c.desc=desc
    c.save()
