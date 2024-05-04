from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [

    # path('', views.index, name='index'),
    # path('projects/', views.projects_list, name='projects_list'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectsListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('feedback/', views.feedback_view, name='feedback'),
    # path('project/new/', views.create_project, name='create_project'),
    # path('project/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project'),
    path('project/create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('project/<int:project_id>/add_task/', views.TaskCreateView.as_view(), name='add_task_to_project'),
    # path('project/<int:project_id>/update/', views.update_project, name='update_project'),
    # path('project/<int:project_id>/task/<int:task_id>/update/', views.update_task, name='update_task'),
    path('project/<int:project_id>/update/', views.ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:project_id>/tasks/<int:task_id>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    # path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    # path('project/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('project/<int:project_id>/delete/', views.ProjectDeleteView.as_view(), name='delete_project'),
    path('project/<int:project_id>/tasks/<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
]
