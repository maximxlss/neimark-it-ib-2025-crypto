import random

modulus = 2305843009213693951

key = random.randrange(1, modulus)

pt = random.randrange(1, modulus)

ct = (pt * key) % modulus
print(f"{pt} encrypted to {ct}")

x = random.randrange(1, modulus)

ct = (x * key) % modulus
print(f"x encrypted to {ct}")

guess = int(input("? x = "))
if guess == x:
    print("neimark{REDACTEDREDACTEDREDACTEDREDACTED}")
else:
    print(f"Wrong! {x = }")
