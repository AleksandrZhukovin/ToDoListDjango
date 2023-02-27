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
        'tasks': tasks
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
            t = Task(name=name, status=status, project=p)
            t.save()
    else:
        form = InputTask()

    context = {
        'form': form,
        'tasks': tasks
    }
    return render(request, 'add_tasks.html', context)


def delete_project(request, project_id):
    p = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = InputTask(request.POST)
        if form.is_valid():
            p.delete()
            return redirect('/')
    else:
        form = InputTask()
    context = {
        'title': f'Delete Project {p.name}',
        'form': form
    }
    return render(request, 'delete_pr.html', context)
