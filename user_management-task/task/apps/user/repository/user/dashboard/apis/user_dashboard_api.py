# api
from django.db.models import AutoField

from task.apps.base.views.generic.auth import ApiAuthMixin
from task.apps.user.repository.user.common.apis.user_api import UserAPI


class UserDashboardAPI(ApiAuthMixin ,UserAPI):
    pass
