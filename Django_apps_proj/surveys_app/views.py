from django.shortcuts import render,redirect,HttpResponse
3
def root3(request):
    return HttpResponse("surveys root")
def index3(request):
    return HttpResponse("surveys here")
