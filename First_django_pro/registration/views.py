from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime

def welcome(request):
   
    return render(request,'index.html')
def we(request):
    return render(request,'index.html')

def one_method(request,id2,student):                # no values passed via URL
    context={
        'id2':id2,
        'student':student,
        'evaluation':['first exam','second exam','project','Final'],
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html',context)           

def users_show(request):
    name = request.POST['name']
    id = request.POST['id']
    context = {
        'name':name,
        'id':id
    }
    return render(request,'show.html',context)    
    
# def another_method(request, my_val):	# my_val would be a number from the URL
#     pass                                # given the example above, my_val would be 23
    
# def yet_another(request, name):	        # name would be a string from the URL
#     pass                                # given the example above, name would be 'pooh'
    
# def one_more(request, id, color): 	# id would be a number, and color a string from the URL
#     pass                                # given the example above, id would be 17 and color would be 'brown'
# # Create your views here.
