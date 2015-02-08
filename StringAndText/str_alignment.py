text = 'hello world'
print(text.ljust(20))
print(text.rjust(20, '='))
print(text.center(20, '*'))

print('{:<20}'.format(text))
print('{:=>20}'.format(text))
print('{:*^20}'.format(text))

print('{:-^20}'.format(1.2345))
