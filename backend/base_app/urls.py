from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_view, name='tasks_view'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_edit/<int:pk>/', views.task_edit, name='task_edit'),

]
