from rest_framework import viewsets, generics
from tasks.models import Task
from tasks.permissions import IsAuthor
from tasks.serializers import TasksSerializer


class TasksViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        responsable=None)



