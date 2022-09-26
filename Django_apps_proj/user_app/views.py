from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse

def root(request):
    return redirect('/user')
def index(request):
    return HttpResponse("user here")
