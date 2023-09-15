from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView,UpdateView, DeleteView,ListView
from .permissions import IsTaskCreatorUpdateMixin,IsTaskCreatorDeleteMixin
from .forms import TaskCreateForm
from .models import Task
from django.forms import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
# Create your views here.


class ToDoHomeView(TemplateView):
    template_name = "todos/home.html"


class ToDoTaskCreateView(LoginRequiredMixin,CreateView,IsTaskCreatorUpdateMixin):
    template_name = "todos/task-create.html"
    form_class = TaskCreateForm
    success_url = "/"
    login_url = "/auth/login"
    def form_valid(self, form):
        self.form = form
        task = form.save(commit=False)
        user = self.request.user

        if user.is_authenticated:
            task.owner = user
        else:
            raise ValidationError("You are not logged in")
        return super(ToDoTaskCreateView,self).form_valid(form)

class ToDoListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = "todos/task-list.html"
    login_url = "/auth/login/"
    def get_queryset(self):
        user = self.request.user
        task_list = Task.objects.filter(owner=user)
        return task_list





class ToDoTaskUpdateView(IsTaskCreatorUpdateMixin, UpdateView):
    template_name = "todos/task-create.html"
    form_class = TaskCreateForm
    success_url = "/"
    model = Task


class TaskDeleteView(IsTaskCreatorDeleteMixin, DeleteView):
    model = Task
