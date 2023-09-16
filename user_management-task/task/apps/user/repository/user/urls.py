from django.urls import path, include

urlpatterns = [
    path('website/', include('task.apps.user.repository.user.website.urls')),
    path('dashboard/',
         include('task.apps.user.repository.user.dashboard.urls')),
]
