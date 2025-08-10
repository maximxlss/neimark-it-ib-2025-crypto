import random


p = 2305843009213693951

a = random.randrange(1, p)
b = random.randrange(1, p)
state = random.randrange(1, p)

def lcg():
    global state
    output = state
    state = (a * state + b) % p
    return output


print(f"Output 1: {lcg()}")
print(f"Output 2: {lcg()}")
print(f"Output 3: {lcg()}")

guess = int(input("? Output 4: "))
real = lcg()

if guess == real:
    print("neimark{p4r4m5_r3c0v3r3d_3as1ly_f04f05ab}")
else:
    print(f"Wrong! The right answer was {real}")
