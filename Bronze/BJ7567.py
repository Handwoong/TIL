# 문제 : 그릇

bowl = input()
score = 10

for i in range(1, len(bowl)):
    if bowl[i] != bowl[i-1]:
        score += 10
    else:
        score +=5
print(score)