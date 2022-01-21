# 문제 : 한수

def arithmetic_progression(N):
    count = 0

    if N < 100:
        count = N
    else:
        count += 99

        for i in range(100, N + 1):
            i = str(i)
            idx0, idx1, idx2 = int(i[0]), int(i[1]), int(i[2])
            if idx2 - idx1 == idx1 - idx0:
                count += 1

    return count

N = int(input())
print(arithmetic_progression(N))