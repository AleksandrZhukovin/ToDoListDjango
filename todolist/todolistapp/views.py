from django.urls import reverse_lazy
from .models import Task, Project
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class HomeView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class ProjectView(ListView):
    template_name = 'project.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(project=self.kwargs['project_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Project.objects.get(id=self.kwargs['project_id']).name
        context['project_id'] = self.kwargs['project_id']
        context['tasks'] = self.get_queryset()
        return context


class AddProjectView(CreateView):
    model = Project
    template_name = 'add_project.html'
    fields = ['name']
    success_url = reverse_lazy('index')


class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    success_url = reverse_lazy('index')


class UpdateProjectView(UpdateView):
    model = Project
    fields = ['name']
    template_name = 'edit_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Project.objects.get(id=self.kwargs['pk']).name
        context['tasks'] = Task.objects.filter(project=self.kwargs['pk']).order_by('priority')
        return context


class AddTaskView(CreateView):
    model = Task
    fields = ['name', 'priority', 'deadline', 'status']
    template_name = 'add_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Project.objects.get(id=self.kwargs['project_id']).name
        context['project'] = Project.objects.get(id=self.kwargs["project_id"])
        context['tasks'] = Task.objects.filter(project=self.kwargs['project_id']).order_by('priority')
        self.success_url = f'/add_tasks{self.kwargs["project_id"]}/'
        return context

    def form_valid(self, form):
        form.instance.project = self.get_context_data()['project']
        return super().form_valid(form)


class EditTaskView(UpdateView):
    model = Task
    fields = ['name', 'priority', 'deadline', 'status']
    template_name = 'edit_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.get(id=self.kwargs['pk'])
        self.initial = {'name': task.name, 'status': task.status, 'priority': task.priority,
                        'deadline': task.deadline}
        context['title'] = f'Edit {task.name}'
        self.success_url = f'/edit_project{self.kwargs["project_id"]}/'
        return context

    def get_success_url(self):
        return f'/edit_project{self.kwargs["project_id"]}/'


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'

    def get_success_url(self):
        project = Task.objects.get(id=self.kwargs['pk']).project
        return f'/edit_project{project.id}'
