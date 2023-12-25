from django.shortcuts import redirect
from . import serializers as serializers__API
from .. import models
from rest_framework.decorators import action
from rest_framework import viewsets, response, permissions
import datetime


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers__API.CommentSerializer

    @action(detail=False, methods=["POST"])
    def showAllComments(self, request):
        result = models.Comment.objects.filter(article__id=request.data["id"])
        return response.Response(
            CommentViewSet.serializer_class(result, many=True).data
        )

    @action(detail=False, methods=["POST"])
    def addComment(self, request):
        if not request.user.is_authenticated:
            return response.Response({"message": "Only registered users can add comments"})
        # if comment filed is empty: dont send form
        elif request.data["text"] == "":
            return
        else:
            models.Comment.objects.create(
                text=request.data["text"],
                publish_date=datetime.date.today(),
                author=request.user,
                article=models.NewsArticles.objects.get(id=request.data["id"]),
            )
            # get last added comment of the article
            result = models.Comment.objects.filter(
                article__id=request.data["id"]
            ).order_by("publish_date")
            return response.Response(
                CommentViewSet.serializer_class(result, many=True).data
            )
