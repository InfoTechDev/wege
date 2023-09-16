from django.urls import path, include

from task.apps.user.repository.auth.login import LoginAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),

]
