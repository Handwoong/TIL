# 문제 : 단어 공부

s = input()
s = s.upper()
x = set(s)
x = list(x)

result = []
for i in x:
    result.append(s.count(i))

cnt = result.count(max(result))
idx = result.index(max(result))

if cnt != 1:
    print('?')
else:
    print(x[idx])