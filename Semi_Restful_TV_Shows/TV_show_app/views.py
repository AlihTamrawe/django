from multiprocessing import context
from django.shortcuts import render,redirect
from models import *

def root(request):
    return redirect('/shows')

def insert(request):
    context= {
    }
    return render(request,'change.html',context)

def toshownew(request):
    all_shows = Shows.objects.all().values()
    context= {
        'shows':all_shows
    }
    return render(request,'index.html',context)


def edit(request,id):
    field_name= request.POST.get('')
    c = Shows.objects.get(id=id)
    c.field_name = "some new value for field_name"
    c.save()
    context= {

    }
    return render(request,'edit.html',context)

def details(request):
    context= {
    }
    return render(request,'details.html',context)

def deleteme(request,id):
    item = Shows.objects.get(id=id)
    item.delete()
    return redirect('/shows')
