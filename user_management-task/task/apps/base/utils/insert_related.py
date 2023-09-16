class RelatedObjectManager:
    def __init__(self, insert_many_relation):
        self.insert_many_relation = insert_many_relation

    def create_related_objects(self, data, id):
        for object in self.insert_many_relation:
            objects = data.get(object['request_array_name'], [])
            for obj in objects:
                obj_serializer = object['serializer']
                obj_serializer = obj_serializer(data={object['base_id']: id, **obj})
                if obj_serializer.is_valid(raise_exception=True):
                    obj_serializer.save()

    def delete_nonexistent_related_objects(self, data, id):
        for object in self.insert_many_relation:
            objects = data.get(object['request_array_name'], [])
            serializer = object.get('serializer', False)
            many_id = object.get('relation_id', False)
            one_id = object.get('base_id', False)
            if serializer:
                many_ids = [object.get(many_id, -1) for object in objects]
                query = serializer.Meta.model.objects.filter(**{one_id: id})
                for item in query:
                    item_id = getattr(item, many_id)
                    if item_id not in many_ids:
                        item.delete()

    def update_related_objects(self, data, id):
        for object in self.insert_many_relation:
            objects = data.get(object['request_array_name'], [])
            serializer = object.get('serializer', False)
            many_id = object.get('relation_id', False)
            one_id = object.get('base_id', False)
            if serializer:
                instance_id = []
                query = serializer.Meta.model.objects.filter(**{one_id: id})
                many_ids = [obj.get(many_id, -1) for obj in objects]
                for item in query:
                    item_id = getattr(item, many_id)
                    if item_id in many_ids:
                        instance_id.append(item.id)
                for item in objects:
                    many_relations_id = item.get(many_id, False)
                    if many_relations_id and many_relations_id not in instance_id:
                        obj_serializer = serializer(data={object['relation_id']: id, **item})
                        if obj_serializer.is_valid(raise_exception=True):
                            obj_serializer.save()

    def store_many_relation(self, data, id, action="created"):
        if self.insert_many_relation:
            if action == "created":
                self.create_related_objects(data, id)
            elif action == "updated":
                self.delete_nonexistent_related_objects(data, id)
                self.update_related_objects(data, id)