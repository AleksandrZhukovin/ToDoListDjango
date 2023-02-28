from django.shortcuts import render, redirect
from .forms import InputProject, InputTask
from .models import Task, Project


def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
        'title': 'Home'
    }
    return render(request, 'index.html', context)


def project(request, project_id):
    tasks = Task.objects.filter(project=project_id)
    context = {
        'tasks': tasks,
        'title': 'Add Project'
    }
    return render(request, 'project.html', context)


def add_project(request):
    if request.method == 'POST':
        form = InputProject(request.POST)
        if form.is_valid():
            project_n = form.cleaned_data['name']
            p = Project(name=project_n)
            p.save()
            return redirect(f'/add_tasks{p.id}/')
    else:
        form = InputProject()
    context = {
        'form': form
    }
    return render(request, 'add_project.html', context)


def add_tasks(request, project_id):
    tasks = Task.objects.filter(project=project_id)
    p = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = InputTask(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            name = form.cleaned_data['name']
            priority = form.cleaned_data['priority']
            deadline = form.cleaned_data['deadline']
            t = Task(name=name, status=status, priority=priority, project=p, deadline=deadline)
            t.save()
    else:
        form = InputTask()

    context = {
        'form': form,
        'tasks': tasks,
        'title': f'Add Tasks to Project {p.name}'
    }
    return render(request, 'add_tasks.html', context)


def delete_project(request, project_id):
    p = Project.objects.get(id=project_id)
    p.delete()
    return redirect('/')


def edit_project(request, project_id):
    p = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=p).order_by('priority')

    if request.method == "POST":
        form = InputProject(request.POST, initial={'name': p.name})

    else:
        form = InputProject(initial={'name': p.name})

    context = {
        'form': form,
        'tasks': tasks,
        'project': p,
        'title': f'Edit Project {p.name}'
    }
    return render(request, 'edit_project.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = InputTask(request.POST, initial={'name': task.name, 'status': task.status, 'priority': task.priority,
                                                'deadline': task.deadline})

        if form.is_valid():
            task.name = form.cleaned_data['name']
            task.priority = form.cleaned_data['priority']
            task.status = form.cleaned_data['status']
            task.deadline = form.cleaned_data['deadline']
            task.save()
            return redirect(f'/edit_project{task.project.id}/')

    else:
        form = InputTask(initial={'name': task.name, 'status': task.status, 'priority': task.priority,
                                  'deadline': task.deadline})

    context = {
        'form': form,
        'task_id': task_id,
        'title': f'Edit Project {task.project.name}'
    }
    return render(request, 'edit_task.html', context)


def delete_task(request, task_id):
    t = Task.objects.get(id=task_id)
    t.delete()
    return redirect(f'/edit_project{t.project.id}/')


def add_task(request, project_id):
    p = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = InputTask(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            priority = form.cleaned_data['priority']
            status = form.cleaned_data['status']
            deadline = form.cleaned_data['deadline']
            task = Task(name=name, priority=priority, status=status, project=p, deadline=deadline)
            task.save()
            return redirect(f'/edit_project{project_id}/')

    else:
        form = InputTask()

    context = {
        'form': form,
        'title': f'Add Task to Project {p.name}'
    }
    return render(request, 'edit_task.html', context)
