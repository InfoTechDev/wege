import traceback
from functools import partial
from typing import List

from django.db import models, transaction

from django.http import QueryDict
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from .constants import id_not_uuid, item_not_exist
from .utils import is_valid_uuid

from ...utils.error_handling import ErrorHandler


class BaseViewSet(ErrorHandler, ViewSet):
    model = models.Model
    serializer_class = serializers.ModelSerializer
    queryset = None
    filter_keywords = {}
    replace_fields_label = {}
    select_fields = {}
    is_ability_search_options = False
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    multi_object = False
    num_object_which_error_occurred = 0
    __fields = []
    __exclude = []
    visit = False
    group_by = {}
    select_filter = {}
    on_delete = []
    current_user = False
    not_allowed_methods = []
    withComment = True
    APPEND_SLASHt = False
    signals = {}
    append_fields = {}
    HITCOUNT_KEEP_HIT_ACTIVE = None


    def get_queryset( self ):
        return self.queryset

    def get_object( self, id, model=False ):
        if is_valid_uuid(id):
            object_obtained = model.objects.filter(id=id) if model else self.queryset.filter(id=id)
            if object_obtained.exists():
                return object_obtained[0]
            else:
                raise ModuleNotFoundError(item_not_exist)
        else:
            raise ValueError(id_not_uuid)

    def get_q_set( self ):
        return self.model.objects.all()

    def executing_operations_on_object( self, object_, request=None, **kwargs ):
        return self.serializer_class(object_, many=False, **kwargs,
                                     context={'request': request}).data

    def executing_operations_on_objects( self, objects, request, **kwargs ):
        context = kwargs.pop('context', {})
        return self.serializer_class(objects, many=True, context={'request': request, **context}, **kwargs).data

    def get_message_for_specified_item( self, message, specific_error_pos=None ):
        if self.multi_object:
            return {"item number {" + str(self.num_object_which_error_occurred) + "}": message}
        return message

    def get_convenient_message_according_to_action( self, action="created" ):
        auxiliary_verb = " have" if self.multi_object else " has"
        singular = False if self.multi_object or action == "gotten" else True

        return  self.model.__name__  + auxiliary_verb + " been " + action + " successfully"


    @transaction.atomic
    def save_data( self, data, id=None, is_update=False, action="created", **kwargs ):

        with transaction.atomic():
            if is_update:
                object = self.get_object(id)
                serializer = self.serializer_class(object, data=data,
                                                   **kwargs)
                action = "updated"
            else:
                serializer = self.serializer_class(data=data, **kwargs)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return self.response.collect(
                    {'message': self.get_convenient_message_according_to_action(action),
                     "status": status.HTTP_200_OK,
                     "data": serializer.data})

    def do_actions( self, data, id=None, is_update=False, **kwargs ):
        try:
            return self.save_data(data=data, id=id, is_update=is_update, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return self.handle_exception(e)

    def list( self, request, many=True, **kwargs ):
        try:
            query = kwargs.pop('query', False)
            if query:
                self.queryset = self.queryset.filter(**query)
            data = self.executing_operations_on_objects(self.get_queryset(), request, **kwargs)

            params = {'is_paginated': True}
            self.response.paginate(request, data)
            return self.response.collect(
                {'message': self.get_convenient_message_according_to_action(action="gotten"),
                 "status": status.HTTP_200_OK, **params}, is_paginated=True)
        except Exception as e:
            return self.handle_exception(e)

    def retrieve( self, request, pk, **kwargs ):
        try:
            object = self.get_object(pk)
            data = self.executing_operations_on_object(object, request, **kwargs)
            if self.visit:
                self.executing_base_operations_on_object(request, object, self.HITCOUNT_KEEP_HIT_ACTIVE)
            return self.response.collect(
                {'message': self.get_convenient_message_according_to_action(action="gotten"),
                 "status": status.HTTP_200_OK, "data": data})
        except Exception as e:
            return self.handle_exception(e)

    def create( self, request, **kwargs ):
        return self.do_actions(data=request.data, **kwargs)

    def update( self, request, pk=None, partial=False, **kwargs ):
        return self.do_actions(data=request.data, id=pk, is_update=True, partial=partial, request=request, **kwargs)

    def partial_update( self, request, pk=None, **kwargs ):
        return self.update(request, pk=pk, partial=True, **kwargs)

    @transaction.atomic
    def delete_action( self, ids=[], id=False, **kwargs ):
        query = kwargs.get('query', False)
        if query:
            self.model.objects.filter(**query).delete()
        elif id:
            object = self.get_object(id)
            for item in self.on_delete:
                related_item = getattr(object, item)
                related_item.delete()
            object.delete()

        else:
            self.model.objects.filter(id__in=ids).delete()
        return self.response.collect(
            {'message': self.get_convenient_message_according_to_action(action="deleted"),
             "status": status.HTTP_200_OK})

    @transaction.atomic
    def destroy( self, request, pk=False, **kwargs ):
        try:
            return self.delete_action(request.data.get('ids', []), id=pk, **kwargs)
        except Exception as e:
            print(e)
            import traceback
            print(traceback.format_exc())
            return self.handle_exception(e)

    @action(detail=False, methods=['delete'])
    def multi_delete( self, request, **kwargs ):
        try:
            return self.delete_action(request.data.get('ids', []), id=None, **kwargs)
        except Exception as e:
            print(e)
            import traceback
            print(traceback.format_exc())
            return self.handle_exception(e)
