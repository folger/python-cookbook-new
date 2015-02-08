a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print('Find keys in common: ', end ='')
print(a.keys() & b.keys())
print('Find keys in a that are not in b: ', end ='')
print(a.keys() - b.keys())
print('Find (key,value) in common: ', end ='')
print(a.items() & b.items())
print("Make a new dictionary with {'z', 'w'} removed: ", end ='')
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)
