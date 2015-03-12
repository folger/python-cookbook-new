with open('next_.py') as fr:
    try:
        while True:
            line = next(fr)
            print(line, end='')
    except StopIteration:
        print('End'*20)

with open('next_.py') as fr:
    while True:
        line = next(fr, None)
        if line is None:
            print('End'*20)
            break
        print(line, end='')
