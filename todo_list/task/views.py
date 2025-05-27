from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from task.models import TodoList
from task.forms import TaskForm

# Create your views here.
date=datetime.now()
current_datetime= date.strftime("%y-%m-%dT%H:%M")
def home(request):
    
    # if request.method == 'POST':
    #     done = request.POST['done']
    #     date = request.POST['date']
    #     description = request.POST['description']

    #     TodoList.objects.create(
    #         done=done,
    #         date=date,
    #         description=description,
            
    #     )
    #     return redirect('home')
    
    
    
    tasks = TodoList.objects.all().order_by('-id')
    true_list = [item for item in tasks if item.status]
    false_list = [item for item in tasks if not item.status]
    

    context = {
        'true_list': true_list,
        'false_list': false_list,
        'title': 'All tasks page'
    }
    return render(request, 'home.html', context)

def add_task(request):
     if request.method =='POST':
         form = TaskForm(request.POST,request.FILES)
         if form.is_valid():
             form.save()
             return redirect('home')
     else:
         form=TaskForm()
     context={
            'title':'Home Page',
            'current_datetime':current_datetime,
            'form':form
            
        }
     return render(request,'add_task.html',context)

def all_task(request):
    tasks=TodoList.objects.all().order_by('-id')
    true_list=[item for item in tasks if  item.status]
    false_list=[item for item in tasks if not item.status]
    context={
        'true_list':true_list,
        'false_list':false_list,
        'title':'All tasks page'
        
    }
    return render(request,'all_task.html',context)
    
    
    



def task_update(request,id):
    try:
        task=TodoList.objects.get(id=id)
    except TodoList.DoesNotExist:
        return redirect('home')
    

    if request.method == 'POST':
       form= TaskForm(request.POST,request.FILES,instance=task)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
           form=TaskForm(instance=task)
        

        
       
    context = {
        'form': form,
        'task':task,
        'current_datetime':current_datetime,
        'title':'Edit Task'

    }
    return render(request,'task_update.html',context)
   
def task_delete(request, id):
    # try:
    #     student = TodoList.objects.get(id=id)
    #     student.delete()
    #     return redirect('home')
    # except TodoList.DoesNotExist:
    #     return HttpResponse("Student Not Found")   
    task=TodoList.objects.get(id=id)
    task.delete()
    
    return redirect('home')
