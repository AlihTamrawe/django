from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponse

def root2(request):
    return HttpResponse("blogs here")
def index2(request):
    return HttpResponse("surveys here")
