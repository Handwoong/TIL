# 문제 : 더하기 사이클

n = input()

if int(n) < 10:
    n = '0' + n

count = plus = 0
cycle = ""
cycle2 = n

while True:
    if cycle == n:
        break
    
    plus = int(cycle2[0]) + int(cycle2[1]) # 각 자리수 합
    cycle = cycle2[-1] + str(plus)[-1]
    cycle2 = cycle
    count += 1
    
print(count)