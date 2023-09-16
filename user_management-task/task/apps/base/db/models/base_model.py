from uuid import uuid4

from django.db import models

from task.apps.base.db.models.audit_time import BaseAuditTime


class BaseModel(BaseAuditTime):
    id = models.UUIDField(max_length=50, editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True
