import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'status':['exact'],
            'priority':['exact'],
            'due_date':['lte','gte'],
            'created_date':['lte','gte'],
        }