# (c) @ballicipluck & @AbirHasan2005

from base64 import standard_b64encode, standard_b64decode


def str_to_b64(__str: str) -> str:
    str_bytes = __str.encode('ascii')
    bytes_b64 = standard_b64encode(str_bytes)
    return bytes_b64.decode('ascii')


def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    return bytes_str.decode('ascii')
