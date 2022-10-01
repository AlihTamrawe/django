import http
from django.shortcuts import render,redirect,HttpResponse
from .models import Shows,insert2,update2,ShowsManager
from django.contrib import messages
def root(request):
    return redirect('/shows')




def insert(request):
    errors1={}
    if request.POST :
        errors1 = Shows.objects.validate_show(request.POST)
        if not errors1 :
            url = '/shows'
            id = 0
            id = insert2(request.POST)
            url = "/shows/"+str(id)
            message="update Successfully"
            messages.error(request, "sucssful editing")
            if id != 0 :
                return redirect(url)
        else:
            for key, value in errors1.items():
                messages.error(request, value)
    return render(request,'change.html')

def toshownew(request):
    all_shows = Shows.objects.all()
    context= {
        'all_shows':all_shows
    }
    return render(request,'index1.html',context)


def edit(request,id):
    errors={}
    message = "fail to update"
    id1 = Shows.objects.get(id=id)
    if request.POST:
        errors = Shows.objects.validate_show(request.POST)
        if not errors :
            fields= request.POST
            update2(fields,id1)
            print("update Successfully")
            messages.error(request, "succssful editing")
        else:
            for key, value in errors.items():
                messages.error(request, value)
    context= {
        'id':id,
        'message':message,
        'show_id':id1
    }
    return render(request,'edit.html',context)

def details(request,id):
    id_shows = Shows.objects.get(id=id)
    context= {
        'show':id_shows
    }
    return render(request,'details.html',context)

def deleteme(request,id):
    item = Shows.objects.get(id=id)
    item.delete()
    return redirect('/shows')
