import uuid

from rest_framework.test import APITestCase
from rest_framework import status

from core.models import Channel


class ChannelResourceTest(APITestCase):
    def setUp(self):
        self.uid = uuid.uuid4()
        self.channel = Channel.objects.create(
            uuid=self.uid,
            name="starbucks"
        )
        self.response = self.client.get('/api/channels/', format='json')

    def test_should_return_status_200(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_should_return_channel_list(self):
        self.assertEqual(self.response.data, [{
            "uuid": str(self.uid),
            "name": "starbucks"
        }])
