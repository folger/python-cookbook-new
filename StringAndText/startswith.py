import os
if any(name.endswith(('.py', 'pyw')) for name in os.listdir('.')):
    print('python file exists')
