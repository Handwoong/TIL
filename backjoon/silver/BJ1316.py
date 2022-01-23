# 문제 : 그룹 단어 체커
N = int(input())
result = 0

for i in range(N):
    word_alpha = []
    word = input()

    for idx in word:
        if idx in word_alpha:
            if idx != word_alpha[-1]:
                break
        word_alpha.append(idx)
    
    if len(word_alpha) == len(word):
        result += 1
print(result)