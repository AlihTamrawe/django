from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *



def index(request):
    m2=None
    if 'message_save' in request.POST :
        com = request.POST.get('message_inserted')
        # Comments.objects.create(comment=com,poster=request.session['id'])
        Messages.objects.create(message=com,poster=User.objects.get(id=request.session['id']))
        
        # Comments.objects.create(comment="hi",reply=Messages.objects.get(id=1),commander=User.objects.get(id=3))
        print(request.session['id'])
    if 'comment_save' in request.POST:
        print( request.POST.get('mass'))
        id_for_m = request.POST.get('mass')
        comm =  request.POST.get('comment_inserted')
        Comments.objects.create(comment=comm,commander=User.objects.get(id=request.session['id']),reply=Messages.objects.get(id=id_for_m))
    context ={
        'id1':request.session['id'],
        'Messages':Messages.objects.all(),
        'Comments':Comments.objects.all(),
        # 'owner_message':
    }
    return render(request,'index.html',context)