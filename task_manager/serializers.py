from task_manager.models import User, Project, Task, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "date_joined"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"  # Includes project and assignees correctly


class TaskSerializer(serializers.ModelSerializer):
    assignees = UserSerializer(many=True)

    # project = ProjectSerializer() #* add this to change the project id to the actual project info
    class Meta:
        model = Task
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
