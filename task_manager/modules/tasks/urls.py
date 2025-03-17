from .views import handleTasks, handleTaskById
from django.urls import path

tasksUrlPatterns = [
  path('tasks', handleTasks),
  path('tasks/<int:id>', handleTaskById),
]
