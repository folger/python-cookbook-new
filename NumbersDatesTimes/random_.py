import random
values = [1, 2, 3, 4, 5, 6]
for _ in range(5):
    print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

for _ in range(10):
    print(random.randint(0, 10))

for _ in range(3):
    print(random.random())


print(random.getrandbits(200))
