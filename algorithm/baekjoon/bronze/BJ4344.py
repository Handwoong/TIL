# 문제 : 평균은 넘겠지

C = int(input())
for i in range(C):
    count = 0
    N = list(map(int, input().split()))
    aver = sum(N[1:]) / N[0]
    for j in N[1:]:
        if j > aver:
            count += 1
    print("{0:.3f}%".format(count/N[0]*100))