from task_manager.serializers import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task_manager.models import Comment
from rest_framework import status


@api_view(["GET", "POST"])
def handleComments(request, format=None):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def handleCommentById(request, id, format=None):
    try:
        db_comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CommentSerializer(db_comment)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CommentSerializer(db_comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        db_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
