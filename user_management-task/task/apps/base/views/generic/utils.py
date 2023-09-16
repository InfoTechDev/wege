import uuid



def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False





def get_object(object_, value):
    try:
        object_obtained = object_.objects.filter(id=value)
        if object_obtained.exists():
            return object_obtained.first()
        else:
            return False
    except object_.DoesNotExist:
        return False
        # raise Http404


def is_int(val):
    if type(val) == int:
        return True
    else:
        return False


def is_numeric(val: str) -> bool:
    if val.isnumeric():
        return True
    else:
        return False


def get_object_by_user(object_, user):
    try:
        object_obtained = object_.objects.filter(user=user)
        if object_obtained.exists():
            return object_obtained.first()
        else:
            return False
    except object_.DoesNotExist:
        return False
        # raise Http404


