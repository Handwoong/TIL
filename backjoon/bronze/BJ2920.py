# 문제 : 음계

da = {'12345678':'ascending', '87654321':'descending'}

a = input().split()
a = "".join(a)

if a not in da:
    print('mixed')
else:
    print(da[a])