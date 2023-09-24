from django.urls import path
from .views import ToDoHomeView,ToDoTaskCreateView,ToDoTaskUpdateView,ToDoListView,TaskDeleteView,TaskDetailView,TaskCompleteView, ToDoTaskCompleteView
app_name = "todo"
urlpatterns = [
    path('',ToDoHomeView.as_view(),name='home'),
    path('task/create/',ToDoTaskCreateView.as_view(),name='todo-task-create'),
    path('task/<pk>/update/',ToDoTaskUpdateView.as_view(),name='todo-task-update'),
    path('tasks/',ToDoListView.as_view(),name='todo-tasks'),
    path('tasks/completed',TaskCompleteView.as_view(),name='todo-tasks-completed'),
    path('task/<pk>/delete/',TaskDeleteView.as_view(),name='delete'),
    path('task/<pk>/detail/',TaskDetailView.as_view(),name='task-detail'),
    path('task/<pk>/task-complete/', ToDoTaskCompleteView.as_view(), name='todo-task-complete'),

]
