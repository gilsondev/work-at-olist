import uuid

from django.test import TestCase

from core.models import Channel, Category
from core.serializers import ChannelSerializer, CategorySerializer


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

class CategorySerializerTest(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            name="starbucks"
        )

        self.category_root = Category.objects.create(
            channel=self.channel,
            name="Coffee"
        )

        self.subcategory = Category.objects.create(
            channel=self.channel,
            name="Cappuccino",
            parent=self.category_root
        )

    def test_should_serialize_category(self):
        serializer = CategorySerializer(self.category_root)

        self.assertEqual(serializer.data, {
            "uuid": str(self.category_root.uuid),
            "name": "Coffee",
            "subcategories": [
                {
                    "uuid": str(self.subcategory.uuid),
                    "name": "Cappuccino",
                    "subcategories": [] 
                }
            ]
        })
