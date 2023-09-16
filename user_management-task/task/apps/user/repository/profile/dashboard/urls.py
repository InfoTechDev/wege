from django.urls import path, include
from rest_framework.routers import DefaultRouter


from task.apps.user.repository.profile.dashboard.apis.profile_dashboard_api import ProfileDashboardAPI

router = DefaultRouter()
router.register(r'profiles', ProfileDashboardAPI)

urlpatterns = [
    path('', include(router.urls)),
]
