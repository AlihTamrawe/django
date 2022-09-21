from django.shortcuts import render, HttpResponse,redirect
from contextlib import redirect_stderr
from multiprocessing import context
# from time import gmtime, strftime

def root(request):
    return redirect('/blogs')

def index(request):
    context = {
        'Placeholder':'placeholder',

    }
    return  render(request,'index.html',context)
