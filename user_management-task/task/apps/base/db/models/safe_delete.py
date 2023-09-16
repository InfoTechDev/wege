from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel


class BaseSafeDeleteMode(SafeDeleteModel):
    unique_column = []

    class Meta:
        abstract = True

    def clean(self, *args, **kwargs):
        for column in self.unique_column:
            if column and not self.deleted:
                if self.__class__.objects.exclude(pk=self.pk).filter(
                        **{column: getattr(self, column), 'deleted__isnull': True}).exists():
                    raise ValidationError('The ' + str(column) + ": " + str(getattr(self, column)) + ' already exists')

    def save(self, *args, **kwargs):
        self.clean(*args, **kwargs)
        super().save(*args, **kwargs)
