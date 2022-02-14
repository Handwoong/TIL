# 문제 : OX퀴즈

T = int(input())

for i in range(T):
    score = 0
    count = 0
    quiz = input()

    for j in range(len(quiz)):
        if quiz[j] == "O":
            score += 1
            count += 1
        elif quiz[j] == "X":
            for k in range(count):
                score += k
            count = 0
        if j == len(quiz)-1 and quiz[j] == "O":
            for q in range(count):
                score += q
    print(score)