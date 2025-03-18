from task_manager.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task_manager.models import User
from rest_framework import status


@api_view(["GET", "POST"])
def handleUsers(request, format=None):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def handleUserById(request, id, format=None):
    try:
        db_user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(db_user)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = UserSerializer(db_user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        db_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
