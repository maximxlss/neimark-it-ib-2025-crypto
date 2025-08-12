import random


p = 2305843009213693951

x = random.randrange(1, p)

e = 0x10001
c = pow(x, e, p)
print(f"{c = }")

guess = int(input("? x = "))
if guess == x:
    print("neimark{4lm05t_r54_e28e4657}")
else:
    print("Wrong!")
