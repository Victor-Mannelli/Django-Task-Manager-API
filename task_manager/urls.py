from rest_framework.urlpatterns import format_suffix_patterns
from .projects.urls import projectUrlPatterns
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += projectUrlPatterns

urlpatterns = format_suffix_patterns(urlpatterns)