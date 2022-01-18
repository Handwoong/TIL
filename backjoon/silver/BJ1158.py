# 문제 : 요세푸스 문제

def remove():
    result.append(circle[idx])
    del circle[idx]

N, K = map(int, input().split())
circle = list(range(1, N+1))
result = list()
idx = K-1

while True:
    if not circle:
        break
    if idx >= len(circle):
        idx = idx % len(circle)
        remove()
    else:
        remove()
    idx += K-1
print('<'+", ".join(map(str, result))+'>')