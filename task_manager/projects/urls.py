from django.urls import path
from .views import fetchProjectsList

projectUrlPatterns = [
  path('projects/', fetchProjectsList)
]
