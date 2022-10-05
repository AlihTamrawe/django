from multiprocessing import context
from turtle import title
from venv import create
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


from  .models import User

# Create your views here.

def index(request):
    x=request.session['id']
    v='no'
    
    if request.POST:
        print('-------------------------')
        if request.POST["add_book"] =='book':
            errors = Book.objects.validate_Book(request.POST)
            if not errors :
                print('add books')
                title = request.POST['title']
                description=request.POST['description']
                Book.objects.create(title=title,description=description,uploadeder=User.objects.get(id=x))
            else:
                v='yes'
                for key, value in errors.items():
                    messages.error(request, value)
        

 
    context={
        'id1':User.objects.get(id=x),
        'Books':Book.objects.all(),
        'show':'1',
        'validate':v,
    }
    return render(request,'index.html',context)

def like(request,id):
    x=request.session['id']
    print(x)
    if request.POST:
    # Book.objects.last().add(User.objects.get(id=id))
        if request.POST["e_book"] =='book2':
                print('yetttttttttttttttttttttttt')
                id_for_book = request.POST.get('id')
                edit = Book.objects.get(id=id_for_book)
                edit.description=request.POST.get('description2')
                edit.save()
    
    context={
        'id':id,
        'id1':User.objects.get(id=x),
        'user_of_book':User.objects.get(id=Book.objects.get(id=id).uploadeder_id),
        'Books1':Book.objects.get(id=id),
        'books':Book.objects.all(),
        # 'Bookslike':Book.objects.get(id=1).liker.all(),
        'show':'2',
    }
    return render(request,'index.html',context)


def do_like(request,id2):
    user1=User.objects.get(id=request.session['id'])
    Book.objects.get(id=id2).liker.add(user1)
    context={
        'id':id2,
        'id1':User.objects.get(id=request.session['id']),
        'Books1':Book.objects.get(id=id2),
        'books':Book.objects.all(),

        # 'Bookslike':Book.objects.get(id=1).liker.all(),
        'show':'2',
    }
    return redirect(f'/books/{id2}/')
