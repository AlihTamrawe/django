from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponse


def index(request):
    
    if request.GET =='plus' :
        request.session['test'] +=2
        request.session.save()
        if request.session == 'test':
            request.session['test']=0
            request.session.save()
    else:
        request.session['test'] +=1
        request.session.save()
    return render(request,'index.html')

def destroy(request):
    print('canceled')
    request.session['test']=0
    return render(request,'index.html')