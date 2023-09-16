# api
from task.apps.base.views.generic.auth import ApiAuthMixin
from task.apps.base.views.generic.view_set import BaseViewSet
from task.apps.user.repository.profile.common.serializers.profile_serializer import ProfileSerializer
from task.apps.user.repository.profile.model import Profile


class ProfileAPI(ApiAuthMixin, BaseViewSet):
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


