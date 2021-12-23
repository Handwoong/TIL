# 문제 : 사분면

n = int(input())
AXIS = Q1 = Q2 = Q3 = Q4 = 0

for i in range(n):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    else:
        Q4 += 1

print("""Q1: {0}
Q2: {1}
Q3: {2}
Q4: {3}
AXIS: {4}""".format(Q1, Q2, Q3, Q4, AXIS))