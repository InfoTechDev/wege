from django.db import IntegrityError
from django.http import Http404
from rest_framework import exceptions
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError, PermissionDenied

from task.apps.base.core.responses.base_response import BaseResponse


# class HandleException():
#
def handle_exception(e, specific_error_pos=True):
    response = BaseResponse()
    if isinstance(e, Http404):
        return response.collect(
            {'message': "This Endpoint not found", "status": status.HTTP_404_NOT_FOUND})
    if isinstance(e, (ModuleNotFoundError, NotFound)):
        return response.collect(
            {'message': str(e), "status": status.HTTP_404_NOT_FOUND})
    elif isinstance(e, ValidationError):
        return response.collect(
            {'message': (e.detail),
             "status": status.HTTP_400_BAD_REQUEST})
    elif isinstance(e, ValueError):
        return response.collect(
            {'message': str(e), "status": status.HTTP_400_BAD_REQUEST})
    elif isinstance(e, (exceptions.NotAuthenticated,
                        exceptions.AuthenticationFailed)):
        return response.collect(
            {'message': 'Authentication credentials were not provided.', "status": status.HTTP_403_FORBIDDEN})
    elif isinstance(e, PermissionDenied):
        return response.collect(
            {'message': str(e), "status": status.HTTP_403_FORBIDDEN})
    elif isinstance(e, IntegrityError):
        return response.collect(
            {'message': str(e), "status": status.HTTP_400_BAD_REQUEST})
    else:
        return response.collect(
            {'message': 'Something Went Wrong', "status": status.HTTP_500_INTERNAL_SERVER_ERROR})
