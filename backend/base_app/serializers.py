from . models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fiels = '__all__'
        exclude = ['created_at', 'updated_at']