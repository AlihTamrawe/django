from ast import Del
import email
from django.shortcuts import render
from .models import Users
from django.shortcuts import render,redirect,HttpResponse
from datetime import date

def index(request):
    if request.POST.get('insert_into'):
        request.POST.get('password')
        # print(request.POST['insert_into'])
        first = request.POST.get('first_name_from')
        last = str(request.POST.get('last_name_from'))
        email = str(request.POST.get('email_from'))
        age = int(request.POST.get('age_from'))
        Users.objects.create(first_name=first,last_name=last,email_address=email,age=age,created_at="1999-05-12",update_at =(date.today().strftime('%Y-%m-%d')))
    
    if request.POST.get('Delete'):
        id = int(request.POST.get('ids'))
        c = Users.objects.get(id=id)
        c.delete()
    
    context = {
    	"all_the_users": Users.objects.all(),
            }
    return render(request,"index.html", context)