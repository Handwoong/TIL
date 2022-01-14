# 문제 : 열 개씩 끊어 출력하기

s = input()

a = ''
for i in range(len(s)):
    if len(a) == 10:
        print(a)
        a = ''
    a += s[i]
    
print(a)