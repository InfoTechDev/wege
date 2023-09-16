from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task.apps.user.repository.user.dashboard.apis.user_dashboard_api import UserDashboardAPI

router = DefaultRouter()
router.register(r'users', UserDashboardAPI)

urlpatterns = [
    path('', include(router.urls)),
]
