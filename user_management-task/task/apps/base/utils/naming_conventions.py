import re


def convert_from_camel_case_to_space( text ):
    return re.sub("([a-z])([A-Z])", "\g<1> \g<2>", text)
