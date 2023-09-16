# api
from task.apps.base.views.generic.auth import ApiAuthMixin
from task.apps.base.views.generic.view_set import BaseViewSet
from task.apps.user.repository.role.common.serializers.role_serializer import RoleSerializer
from task.apps.user.repository.role.model import Role


class RoleAPI(ApiAuthMixin, BaseViewSet):
    model = Role
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
