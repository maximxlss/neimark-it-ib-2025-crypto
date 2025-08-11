import random

n = random.randint(9000000, 10000000)

s = int(input(f"Введите последние 5 цифр {n}-ого числа фибоначчи: "))

a, b = 0, 1
for i in range(n - 1):
    a, b = b, (a + b) % 100000

if s == b:
    print("neimark{m4th1ng_th1ng_0c380aed}")
else:
    print(f"Неверно! Правильный ответ: {b:05d}")