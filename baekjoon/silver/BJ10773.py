# 문제 : 제로
import sys

input = sys.stdin.readline
K = int(input())
result = []

for i in range(K):
    N = int(input())

    if N != 0:
        result.append(N)
    else:
        result.pop()
print(sum(result))