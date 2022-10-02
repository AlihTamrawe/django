from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    total_charge=1
    quantity_from_form=0
    price_from_form=0
    if request.POST:
        
        p = request.POST
        quantity_from_form = int(str(p.get('quantity')))
        price_from_form = float(str(p.get('price')))
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        request.session['price']=price_from_form
        return redirect('/checkout/')
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkout(request):
    
    context = {
        'order':Order.objects.last(),
        'price':request.session['price'],
    }
    return render(request, "checkout.html",context)