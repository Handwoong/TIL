# 문제 : 벌집
N = int(input())
cnt = 1
x = 1

while N > x:
    x += 6 * cnt
    cnt += 1
print(cnt)
