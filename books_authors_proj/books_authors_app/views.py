
from django.shortcuts import render,redirect
from .models import Authors, Books

def insert(request):
    print("working .....Book......")
    if request.POST.get('add_book') =='Add':
        titles = request.POST.get('titles')
        description =request.POST.get('description')
        Books.objects.create(title=titles,desc=description)
        titles=None
        description=None
        print(" .....done added......")
    context={
        'all_book':Books.objects.all(),
    }
    return render(request,'book.html',context)

def add1(request):
    print(request.POST)
    if request.POST.get('lookr') =='go':
        first_name = request.POST.get('first')
        last =request.POST.get('last')
        note =request.POST.get('note')
        name = first_name+last
        Authors.objects.create(name=name,notes=note)
        name=None
        note=None
        print(" .....author added......")
    context={
        'all_author':Authors.objects.all(),
    }
    print("working .....author......")
    
    return render(request,'author.html',context)

def fun(request,num):
    if request.POST.get('add_authors') =='add':
        ids = request.POST.get('add_authors2')
        Books.objects.get(id=num).publishers.add(Authors.objects.get(id=ids))

    context = {
        'num':num,
        'books':Books.objects.get(id=num),
        'authors':Books.objects.get(id=num).publishers.all().values(),
        'authors2':Authors.objects.all(),

    }
    print("working .....Book2......")
    return render(request,'book2.html',context)

def shows(request,num):
    if request.POST.get('add_book') =='add':
        ids = request.POST.get('add_book2')
        Authors.objects.get(id=num).books.add(Books.objects.get(id=ids))

    context = {
        'num':num,
        'books':Books.objects.all(),
        'b2':Authors.objects.get(id=num).books.all().values(),
        'authors':Authors.objects.get(id=num),

    }
    print("working .....author......")
    return render(request,'author2.html',context)
