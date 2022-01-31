# 문제: 첼시를 도와줘!
n = int(input())

for i in range(n):
    p = int(input())
    price = []
    name = []
    for j in range(p):
        c1, c2 = input().split()
        price.append(int(c1))
        name.append(c2)
    print(name[price.index(max(price))])
