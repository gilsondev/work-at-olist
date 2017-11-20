from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from core.models import Channel
from core.serializers import ChannelSerializer


class ChannelView(generics.ListAPIView):
    """List existing channels"""
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
