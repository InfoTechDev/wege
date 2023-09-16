from django.urls import path, include

urlpatterns = [
    path('dashboard/',include('task.apps.user.repository.role.dashboard.urls')),
]
