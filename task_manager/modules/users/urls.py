from .views import handleUsers, handleUserById
from django.urls import path

usersUrlPatterns = [
  path('users', handleUsers),
  path('users/<int:id>', handleUserById),
]
