# 문제 : 큐
import sys
input = sys.stdin.readline

N = int(input())
queue = list()
for i in range(N):
    s = input().strip()
    if s[:4] == 'push':
        queue.append(s[5:])
    elif s == 'pop':
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif s == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])