from django.db.models.signals import post_save
from django.dispatch import receiver

from task.apps.user.repository.profile.model import Profile
from task.apps.user.repository.user.model import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(name=instance.name, email=instance.email)