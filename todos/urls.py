from django.urls import path
from .views import ToDoHomeView
urlpatterns = [
    path('',ToDoHomeView.as_view(),name='todo-home')
]
