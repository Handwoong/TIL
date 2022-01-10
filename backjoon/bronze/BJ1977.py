# 문제 : 완전제곱수

M = int(input())
N = int(input())

per_sum = []

for i in range(M, N+1):
    temp = 0
    while True:
        if pow(temp, 2) > N:
            break

        if pow(temp, 2) == i:
            per_sum.append(i)
        temp += 1

if not per_sum:
    print(-1)
else:
    print(sum(per_sum))
    print(min(per_sum))