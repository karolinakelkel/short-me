import string
from random import choices


def generate_code(length: int = 5):
    chars = string.ascii_letters + string.digits + '-_'

    return ''.join(choices(chars, k=length))
