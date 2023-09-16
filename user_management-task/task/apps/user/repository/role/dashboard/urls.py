from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task.apps.user.repository.role.dashboard.apis.role_dashboard_api import RoleDashboardAPI

router = DefaultRouter()
router.register(r'roles', RoleDashboardAPI)

urlpatterns = [
    path('', include(router.urls)),
]
