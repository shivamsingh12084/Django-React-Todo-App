from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Converts model instances in json format to work with frontend"""
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "completed")

