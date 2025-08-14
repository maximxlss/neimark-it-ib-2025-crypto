import random


p = 7688572204576988606278207501628554545005756934795134128462697896502552048664027359071216097716582051756864039478434602620847021842666172277576981335764429

a = random.randrange(1, 10 ** 12)
b = random.randrange(1, 10 ** 12)

c = a * pow(b, -1, p) % p
print(f"{c = }")

guess = int(input("? a = "))
if a == guess:
    print("neimark{sup3r_l4tt1c3s_e7ce4fd4}")
else:
    print(f"Wrong! {a = }")
