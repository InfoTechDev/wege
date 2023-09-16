from django.db import models


class BaseAuditTime(models.Model):
    unique_column = []
    created_at = models.DateTimeField('Created At', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
