
modulus = 2305843009213693951

pt = int(input("? pt = "))
ct = int(input("? ct = "))

key = ct * pow(pt, -1, modulus) % modulus

ct = int(input("? x encrypted to "))

x = ct * pow(key, -1, modulus) % modulus

print(f"{x = }")
