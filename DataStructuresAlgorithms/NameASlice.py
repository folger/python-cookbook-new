items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])
items[a] = [10,11]
print(items[a])
del items[a]
print(items[a])
print(a. start, a.stop, a.step)
print('-' * 20)

a = slice(5, 50, 2)
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
