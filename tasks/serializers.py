from rest_framework import serializers

from tasks.models import Task


class TasksSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('author', 'pub_date')

