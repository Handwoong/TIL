# 문제 : 덱

import sys
input = sys.stdin.readline
dequeue = list()
N = int(input())
for i in range(N):
    s = input().strip()

    if s[:10] == 'push_front':
        dequeue.insert(0, s[11:])
    elif s[:9] == 'push_back':
        dequeue.append(s[10:])
    elif s == 'pop_front':
        if not dequeue:
            print(-1)
        else:
            print(dequeue[0])
            del dequeue[0]
    elif s == 'pop_back':
        if not dequeue:
            print(-1)
        else:
            print(dequeue[-1])
            del dequeue[-1]
    elif s == 'size':
        print(len(dequeue))
    elif s == 'empty':
        if not dequeue:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if not dequeue:
            print(-1)
        else:
            print(dequeue[0])
    elif s == 'back':
        if not dequeue:
            print(-1)
        else:
            print(dequeue[-1])