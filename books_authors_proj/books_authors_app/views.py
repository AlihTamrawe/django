from django.shortcuts import render,redirect

def root(request):
    print("working ...........")
    return redirect('/books')

def insert(request):
    
    return render(request,'index.html')
