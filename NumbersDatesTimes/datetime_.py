from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

from datetime import datetime
a = datetime(2012, 10, 23)
print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
print(b - a)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))


from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))
d = relativedelta(b, a)
print(d)
print(d.months)
print(d.days)
