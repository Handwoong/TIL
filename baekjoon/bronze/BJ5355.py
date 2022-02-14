# 문제 : 화성 수학

T = int(input())

for i in range(0,T):
    A = []
    A = list(input().split())

    result = float(A[0])

    for j in range(len(A)):
        if "@" in A[j]:
            result *= 3
        if "%" in A[j]:
            result += 5
        if "#" in A[j]:
            result -= 7
    print("{:.2f}".format(result))
