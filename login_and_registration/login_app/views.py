from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import datetime

def root(request):
    v =datetime.datetime.today()-datetime.datetime.strptime("2002-01-01","%Y-%m-%d" )
    if v/356 < datetime.timedelta(days=13*356):
        print('true ')
    request.session.pop('email',None)
    errors={}
    user=''
    message = ""
    if request.POST:
        if request.POST.get('login')=='log':
            print(request.POST.get('login'))
            email1=request.POST.get('e1')
            pw=request.POST.get('p1')
            if User.objects.filter(email=email1):
                c = User.objects.get(email=email1)
                message = ""
                request.session['email']=email1
                request.session.save()
                if bcrypt.checkpw(request.POST['p1'].encode(), c.password.encode()):
                    print("password match")
                    return redirect('/success')
                else:
                    message = "Wrong password"
                    print('Wrong password')
        if request.POST.get('register') == 'reg':
            print("Register================================================")
            if request.POST.get('pw1') == request.POST.get('pw2'):
                errors = User.objects.validate_register(request.POST)
                if not errors :
                    id =add_user(request.POST)
                    print(id)
                else:
                    for key, value in errors.items():
                        messages.error(request, value)
            else:
                print("confirm is Wrong")
        
    context= {
        'user':user,
        'message':message,

    }
    
    return render(request,'index.html',context)


def index(request):
    if 'email' not in request.session :
        print('deleted')
        return redirect('/')
    context = {
    'users':User.objects.get(email=request.session['email']),
    }
    return render(request,'Show.html',context)

def out(request):
    if request.session['email']:
        request.session.pop('email',None)
        print('deleted')
    return redirect('/')