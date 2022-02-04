# 문제 : 2차원 배열의 합
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
sum_arr = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    arr.append(list(map(int, input().split())))
    for j in range(1, M+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(sum_arr[x][y] - sum_arr[x][j-1] - sum_arr[i-1][y] + sum_arr[i-1][j-1])
