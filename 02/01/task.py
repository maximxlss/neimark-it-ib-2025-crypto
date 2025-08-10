from random import randbytes


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


key = randbytes(32)

print("1.")
pt = b'neimarkneimarkneimarkneimarkneim'
print(f"{pt = }")
ct = xor(pt, key)
print(f"{ct = }")

print("2.")
pt = b'neimark{n0t_s4f3_527ee2cd4cf4cb}'
print("pt = здесь был флаг")
ct = xor(pt, key)
print(f"{ct = }")


