from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<int:project_id>/', views.ProjectView.as_view(), name='project'),
    path('add_project/', views.AddProjectView.as_view(), name='add_project'),
    path('add_tasks<int:project_id>/', views.AddTaskView.as_view(), name='add_tasks'),
    path('delete_project<int:pk>/', views.DeleteProjectView.as_view(), name='delete_project'),
    path('edit_project<int:pk>/', views.UpdateProjectView.as_view(), name='edit_project'),
    path('edit_task<int:pk>/<int:project_id>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task')
]
