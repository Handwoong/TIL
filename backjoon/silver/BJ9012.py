# 문제 : 괄호
import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    S = input().strip()

    stack = []
    for j in S:
        if j == '(':
            stack.append(j)
        else:
            if stack and ')' not in stack:
                stack.pop()
            else:
                stack.append(')')
                break
    if stack:
        print('NO')
    else:
        print('YES')