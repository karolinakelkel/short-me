import string
from random import choices


def generate_code(length: int = 5):
    chars = string.ascii_letters + string.digits + '-_'
    print(1/64 ** 5)


    return ''.join(choices(chars, k=length))

generate_code()