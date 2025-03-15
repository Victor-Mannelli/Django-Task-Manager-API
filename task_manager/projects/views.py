from django.http import JsonResponse
from .serializers import ProjectSerializer
from ..models import Project


def fetchProjectsList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse(serializer.data, safe=False)