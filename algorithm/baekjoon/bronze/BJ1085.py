# 문제 : 직사각형에서 탈출

x, y, w, h = map(int, input().split())
result = []
result.append(x)
result.append(w-x)
result.append(y)
result.append(h-y)
print(min(result))
