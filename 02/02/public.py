from random import randbytes
from math import ceil


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


key = randbytes(5)

pt = b'neimark{REDACTEDREDACTEDREDACT}'
key *= ceil(len(pt) / len(key))

print("pt = здесь был флаг")
ct = xor(pt, key)
print(f"{ct = }")


