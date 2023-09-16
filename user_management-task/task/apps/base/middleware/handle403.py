from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, PermissionDenied):
        response = Response(
            {"detail": "You do not have permission to perform this action."},
            status=403
        )

    return response
