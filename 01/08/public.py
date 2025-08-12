import random


p = 2305843009213693951

a = random.randrange(1, p)
print(f"{a = }")

e = int(input("? e = "))
if pow(a, e, p) == 1:
    print("neimark{REDACTEDREDACTEDREDACTEDREDACTED}")
else:
    print("Wrong!")
