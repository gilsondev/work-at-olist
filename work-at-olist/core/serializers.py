from rest_framework import serializers

from core.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('uuid', 'name',)
