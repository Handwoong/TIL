# 문제 : 주사위 게임

N = int(input())
score = []

for i in range(0, N):
    dice = []
    dice = list(map(int, input().split()))
    dice.sort()

    if dice[0] == dice[1] == dice[2]:
        score.append(10000+(dice[0]*1000))
    elif dice[0] != dice[1] and dice[1] != dice[2] and dice[0] != dice[2]:
        score.append(max(dice)*100)
    else:
        score.append(1000+(dice[1]*100))

print(max(score))