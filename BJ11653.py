# 문제 : 소인수분해

N = int(input())

i = 2

while i <= N:
    if N%i == 0:
        print(i)
        N /= i
    else:
        i += 1