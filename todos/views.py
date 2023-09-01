from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView,UpdateView, DeleteView
from .permissions import IsTaskCreatorUpdateMixin,IsTaskCreatorDeleteMixin
from .forms import TaskCreateForm
from .models import Task
# Create your views here.


class ToDoHomeView(TemplateView):
    template_name = "todos/home.html"


class ToDoTaskCreateView(CreateView,IsTaskCreatorUpdateMixin):
    template_name = "todos/task-create.html"
    form_class = TaskCreateForm
    success_url = "/"


class ToDoTaskUpdateView(IsTaskCreatorUpdateMixin, UpdateView):
    template_name = "todos/task-create.html"
    form_class = TaskCreateForm
    success_url = "/"
    model = Task


class TaskDeleteView(IsTaskCreatorDeleteMixin, DeleteView):
    model = Task
