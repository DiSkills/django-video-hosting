from rest_framework import serializers

from main.models import Category, Video


class CategorySerializer(serializers.ModelSerializer):
    """ Category """

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class VideoSerializer(serializers.ModelSerializer):
    """ Video """

    class Meta:
        model = Video
        fields = ('category', 'title', 'slug', 'description', 'author', 'file', 'created_at', 'preview', 'views')
