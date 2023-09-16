from django.db import models

from task.apps.base.db.models.base_model import BaseModel


class Role(BaseModel):
    STUFF = "Stuff"
    CUSTOMER = 'Customer'
    SUPER_ADMIN = "SuperAdmin"
    TYPE_CHOICES = [
        (STUFF, 'Stuff'),
        (CUSTOMER, 'Customer'),
        (SUPER_ADMIN, 'SuperAdmin'),

    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=CUSTOMER, unique=True)
