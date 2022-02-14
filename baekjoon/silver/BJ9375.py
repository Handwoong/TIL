# 문제 : 패션왕 신해빈
import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    clothes = {}
    for j in range(n):
        name, category = input().split()
        
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    result = 1
    for value in clothes.values():
        result *= (value + 1)
    
    print(result - 1)