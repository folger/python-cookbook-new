import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print('-'*20)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
dates = datepat.findall(text)
for month, day, year in dates:
    print('{}-{}-{}'.format(month, day, year))
