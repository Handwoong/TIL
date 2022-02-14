# 문제 : 크로아티아 알파벳
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
count = len(alpha)

for i in cro_alpha:
    count -= alpha.count(i)
print(count)