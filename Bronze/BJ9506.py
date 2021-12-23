# 문제 : 약수들의 합

while True:
    summea = 0
    meaString = ''
    mea = []
    n = int(input())

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            mea.append(i)
            summea += i
    for j in range(len(mea)):
        meaString += str(mea[j]) + " + "

    if summea == n:
        print("{0} = {1}".format(n, meaString[0:-3]))
    else:
        print("{0} is NOT perfect.".format(n))