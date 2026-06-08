from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Task.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('task_list')

    return render(request, 'tasks/task_add.html')


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
