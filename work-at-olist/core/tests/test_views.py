import uuid

from rest_framework.test import APITestCase
from rest_framework import status

from core.models import Channel, Category


class ChannelResourceTest(APITestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            name="starbucks"
        )
        self.response = self.client.get('/api/channels/', format='json')

    def test_should_return_status_200(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_should_return_channel_list(self):
        self.assertEqual(self.response.data, [{
            "uuid": str(self.channel.uuid),
            "name": "starbucks"
        }])


class CategoryResourceTest(APITestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            name="starbucks"
        )

        self.category_coffee = Category.objects.create(
            channel=self.channel,
            name="Coffee"
        )

        self.category_tea = Category.objects.create(
            channel=self.channel,
            name="Tea"
        )

        self.espresso = Category.objects.create(
            channel=self.channel,
            name="Espresso",
            parent=self.category_coffee
        )
        self.latte = Category.objects.create(
            channel=self.channel,
            name="Latte Macchiato",
            parent=self.category_coffee
        )

        self.iced_tea = Category.objects.create(
            channel=self.channel,
            name="Iced Teas",
            parent=self.category_tea
        )

        self.response = self.client.get('/api/channels/starbucks/categories/',
                                        format='json')

    def test_should_return_status_200(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_should_return_categories_tree(self):
        self.assertListEqual(self.response.json(), [
            {
                "uuid": str(self.category_coffee.uuid),
                "name": "Coffee",
                "subcategories": [
                    {
                        "uuid": str(self.espresso.uuid),
                        "name": "Espresso",
                        "subcategories": []
                    },
                    {
                        "uuid": str(self.latte.uuid),
                        "name": "Latte Macchiato",
                        "subcategories": []
                    }
                ]
            },
            {
                "uuid": str(self.category_tea.uuid),
                "name": "Tea",
                "subcategories": [
                    {
                        "uuid": str(self.iced_tea.uuid),
                        "name": "Iced Teas",
                        "subcategories": []
                    }
                ]
            }
        ])
