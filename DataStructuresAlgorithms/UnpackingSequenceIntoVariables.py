p = (4, 5)
x, y = p
print(x)
print(y)
print()

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)
print()

name, shares, price, (year, month, day) = data
print(year)
print(month)
print(day)
print()

# drop values
_, shares, price, _ = data
print(shares)
print(price)
