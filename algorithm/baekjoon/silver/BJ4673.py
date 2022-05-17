# 문제 : 셀프 넘버

def solve(n):
    num = list(range(1, n+1))
    for i in range(1, n+1):
        x = str(i)
        temp = 0
        for j in range(len(x)):
            temp += int(x[j])
        init = i + temp
        if init in num:
            num.remove(init)
    for k in num:
        print(k)
        
solve(10000)