import random


p = 233435236823993320227084003674250502479733883541105667249258097228256942236683179879224201694501996903281086292605838589312946043860986803958183218677499
p **= 3
g = 2

x = random.randrange(1, p)
h = pow(g, x, p)
print(f"{h = }")

guess = int(input("? x = "))
if x == guess:
    print("neimark{a1m05t_h4rd_n0w_484eb8bc}")
else:
    print(f"Wrong! {x = }")
