# 문제 : Baseball

T = int(input())


for i in range(T):
    Y = 0
    K = 0
    for j in range(9):
        score = []
        score = list(map(int, input().split()))
        Y += score[0]
        K += score[1]

    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")