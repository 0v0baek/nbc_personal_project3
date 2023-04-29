from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Todo
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Todo
        fields = ('id', 'title', 'is_complete', 'user')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "is_complete",)

