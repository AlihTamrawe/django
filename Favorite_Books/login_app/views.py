from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import datetime

def login(request):
    request.session['id']= 0
    user=''
    message = ""
    if request.POST:
        if request.POST.get('login')=='log':
            print(request.POST.get('login'))
            email1=request.POST.get('e1')
            pw=request.POST.get('p1')
            if User.objects.filter(email=email1):
                c = User.objects.get(email=email1)
                print(email1)
                message = ""
                request.session['email']=email1
                request.session.save()
                request.session['id']=c.id
                if bcrypt.checkpw(pw.encode(), c.password.encode()):
                    print("password match")
                    return redirect('/books')
                else:
                    message = "Wrong password"
                    print('Wrong password')
    context= {
        'user':user,
        'message':message,
    }
    
    return render(request,'index1.html',context)

def register(request):
    errors={}
    if request.POST:
        if request.POST.get('register') == 'reg':
                print("Register================================================")
                if request.POST.get('pw1') == request.POST.get('pw2'):
                    errors = User.objects.validate_register(request.POST)
                    if not errors :
                        id =add_user(request.POST)
                        print(id)
                        return redirect('/')
                    else:
                        for key, value in errors.items():
                            messages.error(request, value)
                else:
                    print("confirm is Wrong")
    context ={

    }
    return render(request,'index2.html',context)

# def index(request):
#     if 'email' not in request.session :
#         print('deleted')
#         return redirect('/')
#     return
# def out(request):
#     if request.session['email']:
#         request.session.pop('email',None)
#         print('deleted')
#     return redirect('/')