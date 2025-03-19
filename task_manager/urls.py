from task_manager.modules.projects.urls import projectsUrlPatterns
from task_manager.modules.comments.urls import commentsUrlPatterns
from task_manager.modules.users.urls import usersUrlPatterns
from task_manager.modules.tasks.urls import tasksUrlPatterns
from task_manager.modules.auth.urls import authUrlPatterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += usersUrlPatterns
urlpatterns += projectsUrlPatterns
urlpatterns += tasksUrlPatterns
urlpatterns += commentsUrlPatterns
urlpatterns += authUrlPatterns

urlpatterns = format_suffix_patterns(urlpatterns)
