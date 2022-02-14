# 문제 : TGN

T = int(input())

for i in range(T):
    Tcase = list(map(int, input().split()))
    adrevenue = Tcase[1] - Tcase[2]
    if adrevenue > Tcase[0]:
        print("advertise")
    elif adrevenue < Tcase[0]:
        print("do not advertise")
    else:
        print("does not matter")