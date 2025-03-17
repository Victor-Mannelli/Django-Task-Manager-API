from .views import handleProjects, handleProjectById
from django.urls import path

projectsUrlPatterns = [
  path('projects', handleProjects),
  path('projects/<int:id>', handleProjectById),
]
