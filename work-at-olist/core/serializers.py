from rest_framework import serializers

from rest_framework_recursive.fields import RecursiveField

from core.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('uuid', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer to define recursive data for categories
    Based on:
    http://gilsondev.in/2016/06/09/usando-django-mptt-em-apis-rest/
    """
    subcategories = serializers.ListSerializer(child=RecursiveField())
    class Meta:
        model = Category
        fields = ('uuid', 'name', 'subcategories',)
