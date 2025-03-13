from config.settings.base import AUTH_USER_MODEL
from django.db import models


# Project Model (One to Many with Task)
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self):
        return self.name
