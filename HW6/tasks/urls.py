from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('id/<int:task_id>/', views.task_by_id, name='task_by_id'),
    path('name/<str:task_name>/', views.task_by_name, name='task_by_name'),
]
