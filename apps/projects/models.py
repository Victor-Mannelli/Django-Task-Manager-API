from django.db import models
from config import settings


# Project Model (One to Many with Task)
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self):
        return self.name
