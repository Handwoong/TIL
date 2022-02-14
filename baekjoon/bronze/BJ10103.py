# 문제 : 주사위 게임

N = int(input())
Chang = Sang = 100

for i in range(0, N):
    A, B = map(int, input().split())

    if A > B:
        Sang -= A
    elif A < B:
        Chang -= B

print(Chang, Sang, sep='\n')