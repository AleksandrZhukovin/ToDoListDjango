from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.project, name='project'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_tasks<int:project_id>/', views.add_tasks, name='add_tasks'),
    path('delete_project<int:project_id>/', views.delete_project, name='delete_project'),
    path('edit_project<int:project_id>/', views.edit_project, name='edit_project'),
    path('edit_task<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task<int:task_id>/', views.delete_task, name='delete_task'),
    path('add_task_to<int:project_id>/', views.add_task, name='add_task')
]
