from django.urls import path, include

urlpatterns = [
    # path('website/', include('task.apps.user.repository.profile.website.urls')),
    path('dashboard/',
         include('task.apps.user.repository.user.dashboard.urls')),
]
