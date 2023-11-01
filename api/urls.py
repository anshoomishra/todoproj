from django.urls import path
from .views import ExpiredTaskView

urlpatterns = [
    path('tasks/expired/', ExpiredTaskView.as_view(), name='expired-task-list'),
]