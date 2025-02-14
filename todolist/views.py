from django.shortcuts import render,get_object_or_404,redirect
from . models import Tasks
from django.utils import timezone

def index(request):
    tasks = Tasks.objects.all()
    return render (request,'index.html',{
        'tasks':tasks
    })

def mark_completed(request,id):
    tasks = get_object_or_404(Tasks,id=id)
    tasks.completed = True 
    tasks.save()
    return redirect('home') 

def delete_task(request,id):
    tasks = get_object_or_404(Tasks,id=id)
    tasks.delete()
    return redirect('home') 

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        
        if title:
            Tasks.objects.create(title=title, due_date=due_date,completed=False,time=timezone.now())
    return redirect ('home')      

def edit_task(request,id):
    task = get_object_or_404(Tasks,id=id)
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_due_date = request.POST.get('due_date')
        if new_title:
            task.title = new_title
        if new_due_date:
            task.due_date = new_due_date    
        
        task.save()
        return redirect('home')
    return render (request, 'edit_task.html',{'task':task})