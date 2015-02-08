from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def search_somefile():
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


def demo_deque():
    q = deque()
    q.append(2)
    q.append(3)
    q.append(4)
    q.appendleft(10)
    q.appendleft(20)
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)


if __name__ == '__main__':
    search_somefile()
    #demo_deque()
