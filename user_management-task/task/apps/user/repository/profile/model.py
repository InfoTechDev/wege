from django.contrib.auth.models import AbstractUser
from django.db import models

from task.apps.base.db.models.author_model import BaseAuthorTrackMixinModel
from task.apps.base.db.models.base_model import BaseModel


class Profile(BaseModel, BaseAuthorTrackMixinModel):
    name = models.CharField(max_length=250)
    email = models.EmailField()
