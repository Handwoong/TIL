# 문제 : 수들의 합

S = int(input())
sum = 0
count = 0

for i in range(1, S+1):
    if sum <= S:
        sum += i
        count += 1
    if sum > S:
        count -= 1
        break
print(count)