from rest_framework import serializers

from rest_framework_recursive.fields import RecursiveField

from core.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('uuid', 'name',)


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uuid', 'name',)


class CategorySerializer(BaseCategorySerializer):
    """
    Serializer to define recursive data for categories
    Based on:
    http://gilsondev.in/2016/06/09/usando-django-mptt-em-apis-rest/
    """
    subcategories = serializers.ListSerializer(child=RecursiveField())
    class Meta:
        model = Category
        fields = ('uuid', 'name', 'subcategories',)


class CategoryDetailSerializer(BaseCategorySerializer):
    parents = serializers.SerializerMethodField()
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('uuid', 'name', 'parents', 'subcategories',)

    def get_parents(self, obj):
        data = []
        for parent in obj.get_ancestors():
            data.append(BaseCategorySerializer(parent).data)
        return data

    def get_subcategories(self, obj):
        data = []
        for subcategory in obj.get_descendants():
            data.append(CategorySerializer(subcategory).data)
        return data
