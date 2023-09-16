from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseContentTypeMixinModel(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
