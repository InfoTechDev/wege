from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task.apps.user'

    def ready(self):
        from task.apps.user.signals.user_signal import create_profile # noqa