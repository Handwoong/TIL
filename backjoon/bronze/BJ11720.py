# 문제 : 숫자의 합

n = int(input())
num = input()

result = 0
for i in range(len(num)):
    result += int(num[i])
print(result)