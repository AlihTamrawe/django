from platform import release
from django.db import models

class Shows(models.Model):
    title = models.TextField(max_length=255)
    network = models.TextField(max_length=255)
    release_date = models.DateTimeField(auto_now=True)
    desc = models.TextField(default="none")
def insert2(p):
        titles = p.get('name_from')
        networks =  p.get('network_from')
        date = p.get('date_from')
        desc = p.get('desc_from')
        Shows.objects.create(title=titles,network=networks,release_date=date,desc=desc)
        last = Shows.objects.last()
        return last.id
def update2(p,c):
    titles = p.get('name_from')
    networks =  p.get('network_from')
    date = p.get('date_from')
    desc = p.get('desc_from')
    c.title=titles
    c.network=networks
    c.release_date=date
    c.desc=desc
    c.save()
