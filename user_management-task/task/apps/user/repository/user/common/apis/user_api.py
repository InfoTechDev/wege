# api
from task.apps.base.views.generic.view_set import BaseViewSet
from ..serializers.user_serializer import UserSerializer
from ...model import User


class UserAPI(BaseViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

