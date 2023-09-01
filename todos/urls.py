from django.urls import path
from .views import ToDoHomeView,ToDoTaskCreateView,ToDoTaskUpdateView
urlpatterns = [
    path('',ToDoHomeView.as_view(),name='todo-home'),
    path('task/create/',ToDoTaskCreateView.as_view(),name='todo-task-create'),
    path('task/<pk>/update/',ToDoTaskUpdateView.as_view(),name='todo-task-update')
]
