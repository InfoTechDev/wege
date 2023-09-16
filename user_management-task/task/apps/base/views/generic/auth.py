from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class ApiAuthMixin:
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdminUser, IsAuthenticated,)
    auth_methods = []
    exclude_auth_methods = []

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if "__all__" in self.auth_methods:
            permission_classes = [IsAdminUser, IsAuthenticated]
        elif "__all__" in self.exclude_auth_methods:
            permission_classes = [AllowAny]
        elif str(self.request.method).lower() in self.auth_methods:
            permission_classes = [IsAdminUser, IsAuthenticated]
        elif str(self.request.method).lower() in self.exclude_auth_methods:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]

        return [permission() for permission in permission_classes]