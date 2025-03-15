from .views import handleProjects, handleProjectById
from django.urls import path

projectUrlPatterns = [
  path('projects', handleProjects),
  path('projects/<int:id>', handleProjectById),
]
