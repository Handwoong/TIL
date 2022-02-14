# 문제 : 문자열 반복

T = int(input())


for i in range(T):
    a = []
    a = input().split()
    R = int(a[0])
    S = a[1]
    
    P = ''
    for j in range(len(S)):
        P += S[j]*R
    
    print(P)
