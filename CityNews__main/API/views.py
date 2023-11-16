from django.shortcuts import redirect
from . import serializers as serializers__API
from .. import models
from rest_framework.decorators import action
from rest_framework import viewsets, response, permissions


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers__API.CommentSerializer

    @action(detail=False, methods=["POST"])
    def showAllComments(self, request):
        result = models.Comment.objects.filter(article__id=request.data["id"])
        return response.Response(
            CommentViewSet.serializer_class(result, many=True).data
        )
