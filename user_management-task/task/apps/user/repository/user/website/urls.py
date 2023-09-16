from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task.apps.user.repository.user.website.apis.user_website_api import UserWebsiteAPI

router = DefaultRouter()
router.register(r'users', UserWebsiteAPI)

urlpatterns = [
    path('', include(router.urls)),
]
