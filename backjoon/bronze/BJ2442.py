# 문제 : 별 찍기 - 5
N = int(input())
blank_count = N - 1
star_count = 1

for i in range(N):
    print(' ' * (blank_count - i), end='')
    print('*' * star_count)
    star_count += 2