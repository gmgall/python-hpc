import random

total = 1000000

dentro = 0

for i in range(total):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1:
        dentro += 1

pi = 4.0 * dentro/total

print("O valor aproximado de pi é {}".format(pi))
