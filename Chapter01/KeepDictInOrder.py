from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for k, v in d.items():
    print(k, v)
print('-'* 20)

import json
print(json.dumps(d))
