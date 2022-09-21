from django.shortcuts import render, HttpResponse,redirect

def root(request):
    return 

def index(request,new=0):
    return HttpResponse(f"placeholder is null{new}")

