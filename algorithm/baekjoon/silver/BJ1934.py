# 문제 : 최소공배수

T = int(input())

import math

for i in range(T):
    a, b = map(int, input().split())

    print(math.lcm(a,b))