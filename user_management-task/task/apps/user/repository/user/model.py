import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from task.apps.base.db.models.base_model import BaseModel
from task.apps.user.repository.role.model import Role


class User(AbstractUser, BaseModel):
    id = models.UUIDField(max_length=50, editable=False, primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, db_index=True)
    # todo : change it to uuid field
    is_user_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    status_message = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True, default="CEO")

    country = models.CharField(max_length=100, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    @property
    def name(self):
        if not self.last_name[0]:
            return self.first_name[0].capitalize()

        return f'{self.first_name[0].capitalize()} {self.last_name[0].capitalize()}'