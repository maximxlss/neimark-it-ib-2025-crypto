n = int(input("n = "))

a, b = 0, 1
for i in range(n - 1):
    a, b = b, (a + b) % 100000

print(b)
