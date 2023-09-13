from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView,UpdateView, DeleteView
from .permissions import IsTaskCreatorUpdateMixin,IsTaskCreatorDeleteMixin
from .forms import TaskCreateForm
from .models import Task
from django.forms import ValidationError
# Create your views here.


class ToDoHomeView(TemplateView):
    template_name = "todos/home.html"


class ToDoTaskCreateView(CreateView,IsTaskCreatorUpdateMixin):
    template_name = "todos/task-create.html"
    form_class = TaskCreateForm
    success_url = "/"
    form = None

    def form_valid(self, form):
        self.form = form
        task = form.save(commit=False)
        user = self.request.user

        if user.is_authenticated:
            task.owner = user
        else:
            return False
        return super(ToDoTaskCreateView,self).form_valid(form)
    def get_success_url(self):
        if self.form_valid(self.form):
            return "/"
        return "/auth/login/"




class ToDoTaskUpdateView(IsTaskCreatorUpdateMixin, UpdateView):
    template_name = "todos/task-create.html"
    form_class = TaskCreateForm
    success_url = "/"
    model = Task


class TaskDeleteView(IsTaskCreatorDeleteMixin, DeleteView):
    model = Task
