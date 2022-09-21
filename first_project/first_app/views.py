from django.shortcuts import render, HttpResponse,redirect

def root(request):
    return render()

def index(request,new=0):
    return HttpResponse(f"placeholder is null{new}")

