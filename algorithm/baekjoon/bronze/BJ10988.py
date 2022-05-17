# 문제 : 팰린드롬인지 확인하기

alpabet = input()
pal = 1

for i in range(int(len(alpabet)/2)):
    if alpabet[i] != alpabet[-1-i]:
        pal = 0

print(pal)