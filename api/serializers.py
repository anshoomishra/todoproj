from rest_framework.serializers import ModelSerializer
from todos.models import Task
class ExpiredTaskSerilizers(ModelSerializer):
    class Meta:
        model = Task
        fields = ['title','description']
