# 문제 : 분산처리

# T = int(input())
# from math import *

# for i in range(T):
#     a, b = map(int, input().split())
#     result = pow(a, b, 10)
#     if result != 0:
#         print(result)
#     else:
#         print(10)

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = map(int,input().split())
    c = pow(a,b,10)
    if c:print(c)#만약 C가 0이 아니라면
    else:print(10)