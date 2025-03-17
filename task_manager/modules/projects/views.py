from task_manager.serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task_manager.models import Project
from rest_framework import status


@api_view(["GET", "POST"])
def handleProjects(request, format=None):
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def handleProjectById(request, id, format=None):
    try:
        db_project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProjectSerializer(db_project)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProjectSerializer(db_project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        db_project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
