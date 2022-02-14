# 문제 : 별 찍기 - 4

n = int(input())
for i in range(n):
    print("{0: >{1}}".format('*'*(n-i), n))