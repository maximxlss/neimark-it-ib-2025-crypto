import random


p = 35059
q = 176864076827511001158893419403268046511
N = 2 * p * q + 1 # prime

x = random.randrange(1, N - 1)

g = 2
a = pow(g, x, N)
print(f"{a = }")

guess = int(input("? x mod p = "))
if x % p == guess:
    print("neimark{s3cr3t_fl4g_4fcfcf71}")
else:
    print(f"Wrong! {x % p = }")
