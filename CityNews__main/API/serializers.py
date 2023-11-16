from .. import models
from rest_framework import serializers


class SavedArticlesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    article = serializers.StringRelatedField()

    class Meta:
        model = models.SavedArticles
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True, many=False
    )

    class Meta:
        model = models.Comment
        fields = "__all__"
