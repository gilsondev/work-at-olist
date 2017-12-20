import uuid
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Channel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "channels"


class Category(MPTTModel):
    uuid = models.UUIDField(default=uuid.uuid4)
    channel = models.ForeignKey('Channel', related_name='categories')
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='subcategories', db_index=True)

    class Meta:
        db_table = "categories"
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
