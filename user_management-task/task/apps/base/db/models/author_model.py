from django.db import models

from task.apps.user.repository.user.model import User


class BaseAuthorTrackMixinModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='%(class)s_updated_by')

    class Meta:
        abstract = True
