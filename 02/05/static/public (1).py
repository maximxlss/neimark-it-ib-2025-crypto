import random


# parameters
p = 11201320989097268009089949979515803860144222629870190216389547169818382860084667114102794808251722730632830592283942899442645874651715736482154145210808783
g = 2

# private key
x = random.randrange(1, p)
print(f"{x = }")

# public key
y = pow(g, x, p)

# message
m = random.randrange(1, p)

# encryption
k = random.randrange(1, p)
c1 = pow(g, k, p)
c2 = (m * pow(g, x*k, p)) % p

print(f"{c1 = }")
print(f"{c2 = }")

guess = int(input("? m = "))
if guess == m:
    print("neimark{REDACTEDREDACTEDREDACTED}")
else:
    print(f"Wrong! The right answer was {m = }.")
