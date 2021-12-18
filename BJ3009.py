# 문제 : 네 번째 점

x = []
y = []

for i in range(0,3):
    A, B = list(map(int, input().split()))
    x.append(A)
    y.append(B)

x.sort()
y.sort()

if x[1] == x[0]:
    x_result = x[2]
elif x[1] == x[2]:
    x_result = x[0]

if y[1] == y[0]:
    y_result = y[2]
elif y[1] == y[2]:
    y_result = y[0]

print(x_result, y_result)
