import uuid

from django.test import TestCase

from core.models import Channel
from core.serializers import ChannelSerializer


class ChannelSerializerTest(TestCase):
    def test_should_serialize_channel(self):
        uid = uuid.uuid4()
        channel = Channel.objects.create(
            uuid=uid,
            name="starbucks"
        )
        serializer = ChannelSerializer(channel)

        self.assertEqual(serializer.data, {
            "uuid": str(uid),
            "name": "starbucks"
        })
