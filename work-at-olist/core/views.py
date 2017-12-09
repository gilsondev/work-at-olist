from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from core.models import Channel, Category
from core.serializers import ChannelSerializer, CategorySerializer


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
