# 백준(7785번) : 회사에 있는 사람
n = int(input())

company = {}
for i in range(n):
    name, inout = input().split()
    company[name] = inout

    if company[name] == 'leave':
        del company[name]

result = list(company.keys())
result.sort()

for j in reversed(result):
    print(j)