import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimeters = fields[1::2] + ['']
print(values)
print(delimeters)
print(''.join(v+d for v,d in zip(values, delimeters)))

print(re.split(r'(?:;|,|\s)\s*', line))
