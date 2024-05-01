from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('task_list')  # Redirect to the task list page after saving the task
    else:
        form = TaskForm()
    
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
