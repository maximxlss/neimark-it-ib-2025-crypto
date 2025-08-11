from random import randbytes
from math import ceil


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


key = randbytes(5)

pt = b'neimark{a1s0_n0t_s4f3_99cd8425}'
key *= ceil(len(pt) / len(key))

print("pt = здесь был флаг")
ct = xor(pt, key)
print(f"{ct = }")


