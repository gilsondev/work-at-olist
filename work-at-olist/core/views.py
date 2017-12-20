from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from core.models import Channel, Category
from core.serializers import (
    ChannelSerializer,
    CategorySerializer,
    CategoryDetailSerializer
)


class ChannelView(generics.ListAPIView):
    """List existing channels"""
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CategoryView(APIView):
    """List all categories and subcategories of a channel"""
    def get(self, request, slug):
        categories = Category.objects.root_nodes()
        categories = categories.filter(channel__name__iexact=slug)
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class CategoryDetailView(APIView):
    """Return a single category with their
    parent categories and subcategories"""
    def get(self, request, uid):
        category = get_object_or_404(Category, uuid=uid)

        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)
