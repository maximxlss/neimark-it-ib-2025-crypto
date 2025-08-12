import random


p = 2305843009213693951

a = random.randrange(1, p)
print(f"{a = }")

a_inv = int(input("? a^-1 = "))

if a * a_inv % p == 1:
    print("neimark{REDACTEDREDACTEDREDACTED}")
else:
    print("Wrong!")
