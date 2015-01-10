mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])
print('-'*20)

for x in (n for n in mylist if n > 0):
    print(x, end=' ')
print()
print('-'*20)


values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)
print('-'*20)


print([n if n > 0 else 0 for n in mylist])
print([n if n < 0 else 0 for n in mylist])
print('-'*20)

addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = (n > 5 for n in counts)
print(list(compress(addresses, more5)))
