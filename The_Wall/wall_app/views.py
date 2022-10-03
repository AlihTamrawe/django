from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *



def index(request):
    if request.POST:
        com = request.POST.get('message_inserted')
        # Comments.objects.create(comment=com,poster=request.session['id'])
        Messages.objects.create(message=com,poster=User.objects.get(id=request.session['id']))
        # Comments.objects.create(comment="hi",reply=Messages.objects.get(id=1),commander=User.objects.get(id=3))
        print(request.session['id'])
    context ={
        'id1':request.session['id'],
        'Messages':Messages.objects.all(),
        # 'owner_message':
    }
    return render(request,'index.html',context)