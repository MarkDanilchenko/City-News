from .. import models
from rest_framework import serializers


class SavedArticlesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    article = serializers.StringRelatedField()

    class Meta:
        model = models.SavedArticles
        fields = "__all__"
