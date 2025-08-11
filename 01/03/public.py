import random


p = 2305843009213693951

x = random.randrange(1, p)

y = (x ** 2 + 7 * x + 2) % p

print(f"{y = }")

guess = int(input("? x = "))
if guess == x or guess == (-7 - x) % p:
    print("neimark{REDACTEDREDACTEDREDACTEDREDACTED}")
else:
    print(f"Wrong! {x = }")
