from django.shortcuts import render,redirect
from .models import Task
from tasks.models import *
from django.shortcuts import render

def create_task(request):
    user_data = UserReg.objects.all()
    task_data = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        assigned_to = request.POST.get('assigned_to')
        
        user_tasks = Task.objects.filter(assigned_to=assigned_to).count()
        if user_tasks < 3:
            assigned = UserReg.objects.get(id=assigned_to)
            task = Task(title=title, description=description, assigned_to =assigned)
            task.save()
            
            return redirect('create_task')
        else:
            return render(request, 'tasks/user_limit.html', {})
        
    return render(request, 'tasks/create_task.html', {'user_data': user_data, 'task_data':task_data})

def update_status(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        task.status = status
        task.save()
        return redirect('create_task')
    return render(request, 'tasks/update_status.html', {'task': task})

def list_users(request):
    users = UserReg.objects.all()
    users_list = []
    
    for user in users:
        
        tasks_count = Task.objects.filter(assigned_to=user).count()
        
        if tasks_count > 0:
            completed_tasks_count = Task.objects.filter(assigned_to=user, status=2).count()
            print(completed_tasks_count)
            if tasks_count == completed_tasks_count:
                users_list.append(user)

    print(users_list)
    return render(request, 'tasks/lists_users.html', {'users_list': users_list,})
    
def sort_users(request):
    users = UserReg.objects.all()
    users_list = []
    order = Task.objects.order_by("time_stamp")
    # print("aaaa",order)
    for user in users:
        tasks_count = Task.objects.filter(assigned_to=user).count()
        if tasks_count > 0:
            completed_tasks_count = Task.objects.filter(assigned_to=user, status=2)
            
            if tasks_count == completed_tasks_count.count():
                users_list.append(user)
                
   
    return render(request, 'tasks/sort_users.html', {"users_list":users_list})
