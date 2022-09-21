from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponse


def index(request):
    if  request.session:
        request.session['count']+=1
        request.session.save()
    else:
        request.session['count'] = 0
        request.session.save()
    return render(request,'index.html')

def destroy(request):
    request.session['count']=0
    request.session.save()
    return redirect('/counter')