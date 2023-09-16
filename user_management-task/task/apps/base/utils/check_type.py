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
