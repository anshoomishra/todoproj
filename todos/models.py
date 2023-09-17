from django.db import models
from account.models import ToDoUser
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse

PRIORITY_CHOICES = (
    ("1", "TOP"),
    ("2", "MID"),
    ("3", "LOW"),

)


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TaskQuerySet(models.QuerySet):

    def get_active(self):
        return self.filter(active=True)

    def get_inactive(self):
        return self.filter(active=False)

    def get_completed(self):
        return self.filter(is_completed=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | Q(description__contains=query))
        return self.filter(lookups).distinct()


class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def get_by_id(self, id):
        queryset = self.get_queryset().filter(id=id)
        if queryset.count() == 1:
            return queryset.first()
        return None

    def search(self, query):
        return self.get_queryset().get_active().search(query)

    def all(self):
        return self.get_queryset().get_active()

    def all_inactive(self):
        return self.get_queryset().get_inactive()


class Task(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(ToDoUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default="LOW")
    due_date = models.DateTimeField(default=one_week_hence)
    objects = TaskManager()
    class Meta:
        ordering = ["due_date"]
        permissions = [("can_be_assigned", "Can Be Assigned to User"), ]

    def get_absolute_url(self):
        return reverse(
            "detail", args=[str(self.id), str(self.id)]
        )
    def __str__(self):
        return self.title
