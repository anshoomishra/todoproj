from django.views.generic import TemplateView, DetailView, FormView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,View
from .permissions import IsTaskCreatorUpdateMixin, IsTaskCreatorDeleteMixin
from .forms import TaskCreateForm, TaskCompleteForm
from .models import Task
from django.forms import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import logging

# Create your views here.

logger = logging.getLogger(__name__)


class ToDoHomeView(TemplateView):
    template_name = "todos/home.html"


class ToDoTaskCreateView(LoginRequiredMixin, CreateView, IsTaskCreatorUpdateMixin):
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
        return super(ToDoTaskCreateView, self).form_valid(form)


class ToDoListView(LoginRequiredMixin, ListView):
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
    template_name = "todos/task-delete-confirm.html"
    success_url = reverse_lazy("todo:todo-tasks")


class ToDoTaskCompleteView(LoginRequiredMixin,FormView):
    template_name = "todos/todo-task-complete-confirm.html"
    form_class = TaskCompleteForm
    success_url = reverse_lazy("todo:todo-tasks")

    def post(self, request, *args, **kwargs):
        logger.info(f"Post from {self.__class__.__name__},{request},{args},{kwargs}")
        return super(ToDoTaskCompleteView,self).post(request, *args, **kwargs)

class TaskCompleteView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "todos/task-list.html"
    login_url = "/auth/login/"

    def get_queryset(self):
        user = self.request.user
        task_list = Task.objects.all().filter(is_completed=False, owner=user)
        return task_list


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todos/task-details.html"
    login_url = "/auth/login/"
    pk_url_kwarg = 'pk'
