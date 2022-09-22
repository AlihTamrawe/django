from http.client import HTTPResponse
from django.shortcuts import render,redirect,HttpResponse


def index(request):
    if request.session == 'test':
        # count=request.session['count']
        # count+=1
        # request.session['test']=count
        # request.session['count']=request.session['test']
        # request.session.save()
        pass
    else:
        request.session['test'] +=1
        request.session.save()
    
    return render(request,'index.html')

def destroy(request):
    print('canceled')
    request.session['test']=0
    return render(request,'index.html')