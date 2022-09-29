import http
from django.shortcuts import render,redirect,HttpResponse
from .models import Shows,insert2,update2

def root(request):
    return redirect('/shows')




def insert(request):
    if request.POST :
        url = '/shows'
        id = 0
        id = insert2(request.POST)
        url = "/shows/"+str(id)
        if id != 0 :
            return redirect(url)
    return render(request,'change.html')

def toshownew(request):
    all_shows = Shows.objects.all()
    context= {
        'all_shows':all_shows
    }
    return render(request,'index1.html',context)


def edit(request,id):
    messages = "fail to update"
    id1 = Shows.objects.get(id=id)
    if request.POST:
        fields= request.POST
        update2(fields,id1)
        print("update Successfully")
        messages="update Successfully"
    context= {
        'id':id,
        'message':messages,
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
