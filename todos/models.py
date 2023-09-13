from django.db import models
from account.models import ToDoUser
from django.utils import timezone

PRIORITY_CHOICES = (
    ("1", "TOP"),
    ("2", "MID"),
    ("3", "LOW"),

)
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(ToDoUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=3,choices=PRIORITY_CHOICES,default="LOW")
    due_date = models.DateTimeField(default=one_week_hence)
    class Meta:
        permissions = [("can_be_assigned","Can Be Assigned to User"),]
    def __str__(self):
        return self.title

