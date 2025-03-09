from apps.projects.models import Project
from apps.users.models import User
from django.db import models


# Task Model (Many to One with Project, Many to Many with Users)
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    assignees = models.ManyToManyField(User, related_name="tasks_assigned")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title
