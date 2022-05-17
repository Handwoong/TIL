# 문제 : Yangjojang of The Year

T = int(input())

for testcase in range(T):
    N = int(input())
    x = []
    y = []
    for i in range(N):
        school, soju = input().split()
        soju = int(soju)
        x.append(school)
        y.append(soju)
    print(x[y.index(max(y))])