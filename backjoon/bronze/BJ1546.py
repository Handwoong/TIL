# 문제 : 평균
aver_list = []
n = int(input())
score = list(map(int, input().split()))
for i in range(n):
    aver_list.append(score[i] / max(score) * 100)
print(sum(aver_list)/len(score))