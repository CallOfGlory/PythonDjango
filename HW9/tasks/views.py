from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    list — усі задачі
    retrieve — задача по id
    create — створення
    update / partial_update — оновлення
    destroy — видалення
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer