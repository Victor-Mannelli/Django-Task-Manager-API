from task_manager.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task_manager.models import Task
from rest_framework import status


@api_view(["GET", "POST"])
def handleTasks(request, format=None):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def handleTaskById(request, id, format=None):
    try:
        db_task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(db_task)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = TaskSerializer(db_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        db_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
