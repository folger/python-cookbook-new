from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

print(d + relativedelta(weekday=FR))
print(d + relativedelta(weekday=FR(-1)))
