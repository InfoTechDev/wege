from django.urls import path, include

urlpatterns = [
    path('', include(('task.apps.user.repository.user.urls'))),
    path('', include(('task.apps.user.repository.role.urls'))),
    path('', include(('task.apps.user.repository.profile.urls'))),
    path('', include(('task.apps.user.repository.auth.urls'))),
]
