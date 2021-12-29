# 문제 : 10부제

day = int(input())
carnum = list(map(int, input().split()))
# count = 0

# for i in range(len(carnum)):
#     if day == carnum[i]:
#         count += 1

# print(count)

print(carnum.count(day))