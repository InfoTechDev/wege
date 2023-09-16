from django.urls import path, include

v1_patterns = [
    path('', include(('task.apps.user.urls', 'api'))),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
