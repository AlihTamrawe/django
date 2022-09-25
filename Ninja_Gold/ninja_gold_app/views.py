from multiprocessing import context
from operator import contains
from django.shortcuts import render,redirect
from time import gmtime, strftime
from django.shortcuts import render


def root(request):
    request.session.clear()
    if  'golds' not in request.session :
        request.session['golds']=0
        request.session['result']=[]
        request.session['count']=0
        
        print("working ...........")
    return redirect('/process_money')

def process(request):
    length1 =0 
    contain = []
    color="green"
    # if request.POST['actions'] =='btn1':

    time=strftime("%Y-%m-%d %H:%M %p ", gmtime())
    if 'kill' in request.POST :
        session_for=request.POST['kill']
        print(session_for)
        if session_for =='btn1':
            request.session['golds']+=20
            result1=str("your entered a farm and earned 15 gold. "+str(time))
            request.session['result'].append(result1) 
            request.session['count']+=1
        print("11")
        if session_for == 'btn2':
            request.session['golds']+=10
            result1=str("your entered a cave and earned 15 gold. "+str(time))
            request.session['result'].append(result1) 
            request.session['count']+=1
            print("22")
        
        if session_for =='btn3':
            request.session['golds']+=20
            result1=str("your entered a House and earned 15 gold. "+str(time))
            request.session['result'].append(result1) 
            request.session['count']+=1
        
        if session_for =='btn4':
            request.session['golds']-=50
            result1=str("so sorry you lost 50 "+str(time))
            request.session['result'].append(result1) 
            request.session['count']+=1
            color="red"
            
    request.session.save()
    context = {
            'x':request.session['golds'],
            'g':request.session['result'],
            't':request.session['count'],
            'color':color
        }
    
    return render(request,'index.html',context)


