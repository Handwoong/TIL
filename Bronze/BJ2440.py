# 문제 : 별 찍기 - 3

# n = int(input())

# for i in range(n):
#     for j in range(n-i):
#         print('*', end = "")
#     print()

n = int(input())

for i in range(n):
    print("*" * (n-i))