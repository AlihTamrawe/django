import numbers
from django.shortcuts import render,redirect
import random 	                 


def callculate(request):
    color ='white'
    result = ' '
    number=request.session['number']
    print(number)
    if request.GET:
        print(request.GET)
        answe = (request.GET['answer'])
        answer = int(answe)
        if answer == number:
            color = 'green'
            result =f"{number} was the <br> number!"
        if answer > number :
            color = 'red'
            result = "Too High !"
        if answer < number :
            color = 'red'
            result = "Too Low !"
    context = {
        'color':color,
        'result':result,
    }
    return render(request,'index.html',context)

def root(request):
    number = random.randint(1, 100) 
    request.session['number']=number
    return redirect('/generate')

