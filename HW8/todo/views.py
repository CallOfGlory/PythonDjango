from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()

    grouped_tasks = {}
    for task in tasks:
        category = task.category
        if category not in grouped_tasks:
            grouped_tasks[category] = []
        grouped_tasks[category].append(task)

    context = {
        'grouped_tasks': grouped_tasks,
        'tasks': tasks
    }

    return render(request, 'todo/task_list.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Завдання успішно додано!')
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'todo/task_form.html', {'form': form, 'title': 'Додати завдання'})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Завдання успішно оновлено!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/task_form.html', {'form': form, 'title': 'Редагувати завдання'})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Завдання успішно видалено!')
        return redirect('task_list')

    return render(request, 'todo/task_confirm_delete.html', {'task': task})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    status = 'виконаним' if task.completed else 'невиконаним'
    messages.success(request, f'Завдання відмічено як {status}!')
    return redirect('task_list')
