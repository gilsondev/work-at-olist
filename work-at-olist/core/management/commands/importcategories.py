import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from core.models import Channel, Category


class Command(BaseCommand):
    help = 'Import categories of channel'

    def add_arguments(self, parser):
        parser.add_argument(
            'channel_name',
            type=str,
            help='Name of Channel to create or update'
        )
        parser.add_argument(
            'channel_file',
            type=str,
            help='Path of categories file to import'
        )

    def handle(self, *args, **kwargs):
        channel_name = kwargs['channel_name']
        channel_path = kwargs['channel_file']

        channel, created = Channel.objects.get_or_create(name=channel_name)

        if created:
            self.stdout.write('Channel {channel} created!'.format(
                channel=channel_name))
        else:
            self.stdout.write('Channel {channel} found.'.format(
                channel=channel_name))

        self._fetch_categories(channel_path, channel)

        total = Category.objects.filter(channel=channel).count()
        self.stdout.write(self.style.SUCCESS(
            '{total} categories created sucessfully!'.format(total=total)))

    def _fetch_categories(self, channel_path, channel):
        self.stdout.write('Importing categories...')

        with open(channel_path) as channelfile:
            reader = csv.reader(channelfile,
                                delimiter=settings.DELIMITER_CATEGORIES_FILE)

            for row in reader:
                self._import_categories(channel, row)

    def _import_categories(self, channel, categories):
        parent = None
        for category in categories:
            name = category.strip()
            category, _ = Category.objects.get_or_create(
                channel=channel,
                name=name,
                parent=parent
            )

            parent = category
