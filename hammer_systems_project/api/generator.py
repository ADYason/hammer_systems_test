import random
import string


def code_generator(k: int, pool: str = string.hexdigits):
    token = ''.join(random.choices(pool, k=k))
    seen = token
    return seen
