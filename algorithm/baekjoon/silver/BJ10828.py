# 문제 : 스택

import sys
input = sys.stdin.readline
N = int(input())
result = []

for i in range(N):
    cmd = input().strip()
    if cmd[:4] == 'push':
        result.append(cmd[5:])
    elif cmd == 'pop':
        if not result:
            print(-1)
        else:
            print(result.pop())
    elif cmd == 'size':
        print(len(result))
    elif cmd == 'empty':
        if not result:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if not result:
            print(-1)
        else:
            print(result[-1])