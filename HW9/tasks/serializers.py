from datetime import date

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    days_left = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'deadline', 'days_left']
        read_only_fields = ['id', 'created_at', 'days_left']

    def get_days_left(self, obj):
        if obj.deadline is None:
            return None
        delta = obj.deadline - date.today()
        return delta.days