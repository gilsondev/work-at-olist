import os

from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from django.apps import apps

from core.models import Channel, Category


CATEGORIES_TEST_PATH = os.path.join(
    apps.get_app_config('core').path,
    'tests',
    'categories_test.csv'
)


class ImportCategoriesManagementTest(TestCase):
    def setUp(self):
        self.out = StringIO()
        call_command('importcategories', 'channel_test',
                     CATEGORIES_TEST_PATH, stdout=self.out)

    def test_should_return_output_before_import(self):
        self.assertIn('Importing categories...', self.out.getvalue())

    def test_should_create_a_category_that_not_exists(self):
        self.assertIn('Channel channel_test created!', self.out.getvalue())

    def test_should_retrieve_a_category_that_exists(self):
        Channel.objects.create(name='other_channel')

        self.out = StringIO()
        call_command('importcategories', 'other_channel',
                     CATEGORIES_TEST_PATH, stdout=self.out)

        self.assertIn('Channel other_channel found.', self.out.getvalue())

    def test_should_import_all_categories(self):
        channel = Channel.objects.get(name='channel_test')
        category = Category.objects.filter(channel=channel)

        self.assertEqual(24, category.count())

    def test_should_return_output_after_import(self):
        self.assertIn('24 categories created sucessfully!',
                      self.out.getvalue())
