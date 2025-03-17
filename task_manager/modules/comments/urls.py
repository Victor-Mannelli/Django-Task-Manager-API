from .views import handleComments, handleCommentById
from django.urls import path

commentsUrlPatterns = [
  path('comments', handleComments),
  path('comments/<int:id>', handleCommentById),
]
