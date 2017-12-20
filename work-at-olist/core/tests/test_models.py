from django.test import TestCase
from django.db import IntegrityError

from core.models import Channel, Category

class ChannelModelTest(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            name="starbucks"
        )

    def test_should_insert_a_channel(self):
        self.assertEqual(1, Channel.objects.count())

    def test_should_be_a_unique_channel_name(self):
        with self.assertRaises(IntegrityError):
            Channel.objects.create(name="starbucks")

    def test_should_a_public_unique_identifier(self):
        self.assertIsNotNone(self.channel.uuid)


class CategoryModelTest(TestCase):
    def setUp(self):
        channel = Channel.objects.create(name="starbucks")
        self.category = Category.objects.create(
            channel=channel,
            name="Coffees"
        )

    def test_should_create_a_category(self):
        self.assertEqual(1, Category.objects.count())

    def test_should_a_public_unique_identifier(self):
        self.assertIsNotNone(self.category.uuid)

    def test_should_return_category_represent(self):
        self.assertEqual(str(self.category), "Coffees")
