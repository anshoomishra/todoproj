from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import ExpiredTaskSerilizers
from todos.models import Task
from django.utils import timezone
from rest_framework.generics import UpdateAPIView,CreateAPIView,ListCreateAPIView


# Create your views here.

class NotificationView(APIView):
    def get(self):
        pass

class TaskCompleteView(APIView):
    def get(self):
        pass

class ExpiredTaskView(ListAPIView):
    serializer_class = ExpiredTaskSerilizers
    queryset = Task.objects.filter(due_date__lt=timezone.now())

