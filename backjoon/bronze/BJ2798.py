# 백준(2798번) : 블랙잭
N, M = map(int, input().split())
card_list = input().split()
icard_list = [int(x) for x in card_list]

result = []
for i in range(len(icard_list)):
    for j in range(len(icard_list)-1):
        for k in range(len(icard_list)-2):
            if i == j or i == k or j == k:
                break
            if (icard_list[i] + icard_list[j] + icard_list[k]) <= M:
                result.append(icard_list[i] + icard_list[j] + icard_list[k])

result.sort()
print(result[-1])