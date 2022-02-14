# 문제 : 단어 공부

s = input().upper()
x = list(set(s))

result = []
for i in x:
    result.append(s.count(i))

cnt = result.count(max(result))
idx = result.index(max(result))

if cnt != 1:
    print('?')
else:
    print(x[idx])