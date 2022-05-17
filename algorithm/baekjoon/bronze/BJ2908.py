# 문제 : 상수

a, b = input().split()
ra = rb = ''
for i in range(3):
    ra += a[-1-i]
    rb += b[-1-i]
if ra > rb:
    print(ra)
else:
    print(rb)