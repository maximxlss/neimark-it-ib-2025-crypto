import random


p = 233435236823993320227084003674250502479733883541105667249258097228256942236683179879224201694501996903281086292605838589312946043860986803958183218677499
p **= 2
g = 2

x = random.randrange(1, p)
h = pow(g, x, p)
print(f"{h = }")

guess = int(input("? x = "))
if x == guess:
    print("neimark{REDACTEDREDACTEDREDACTED}")
else:
    print(f"Wrong! {x = }")
