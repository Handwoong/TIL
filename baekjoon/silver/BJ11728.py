# 문제 : 배열 합치기
import sys

input = sys.stdin.readline
lenA, lenB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B
result.sort()
print(" ".join(map(str, result)))
