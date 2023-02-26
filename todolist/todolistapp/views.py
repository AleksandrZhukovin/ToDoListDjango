from django.shortcuts import render, redirect
from .forms import AddForm, DeleteForm, AddProjectForm
from .models import Task, Project


def index(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            redirect('/add_project')
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


def project(request, project_id):
    tasks = Task.objects.filter(project=project_id)
    context = {
        'tasks': tasks
    }
    return render(request, 'project.html', context)


def add_project(request):
    data = ''
    p = Project(name='')
    p.save()
    id = p.id
    if request.method == 'POST':
        form = AddProjectForm(request.POST)

        if form.is_valid():
            project = form.cleaned_data['project_name']
            task = form.cleaned_data['add_task']
            status = form.cleaned_data['status']
            p = Project.objects.get(id=id)
            p.name = project
            p.save()
            t = Task(name=task, status=status, project=p)
            t.save()
            data = Task.objects.filter(project=id)

    else:
        form = AddProjectForm()

    return render(request, 'add_project.html', {'task': data, 'form_input': form})


def test(request):
    val = ''
    data = Task.objects.order_by('name')
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            val = 'OK'
    else:
        form = AddForm()
    return render(request, 'test.html', {'val': val, 'tasks': data})


"""def inputting(request):
    data = ''
    if request.method == 'POST':
        form = Input(request.POST)

        if form.is_valid():
            data = form.cleaned_data['input_field']

    else:
        form = Input()
    return render(request, 'test.html', {'data': data, 'form': form})"""