from django.shortcuts import render,redirect
from django.shortcuts import render
from .models import Dojos,Ninjas
from django.contrib import messages


def root(request):
    print("working ...........")
    return redirect('/dojos')

def insert(request):
    print(request.POST.get('dojo'))
   
    if request.POST.get('dojo') =='add1' :
        errors = Ninjas.objects.validate_ninja(request.POST)
        if errors > 0:
            name=request.POST.get('name_from')
            print("submiting ...........")
            city= request.POST.get('city_from')
            state = request.POST.get('state_from')
            desc = request.POST.get('desc_from')
            Dojos.objects.create(name=name,city=city,state=state,)
        elif request.POST.get('dojo') =='addt':
            first_name=request.POST.get('first_name_from')
            print("submiting ...........")
            last_ame= request.POST.get('last_name_from')
            dojoi = request.POST.get('ids')
            Ninjas.objects.create(first_name=first_name,last_ame=last_ame,Dojo=Dojos.objects.get(id=dojoi))
        else:
            for key, value in errors.items():
                messages.error(request, value)
    
    context = {
    "all_the_dojo": Dojos.objects.values(),
    "all_the_ninja":Ninjas.objects.values(),

            }
    return render(request,'index.html',context)


