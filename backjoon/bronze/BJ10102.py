# 문제 : 개표

V = int(input())
vote = input()

A = vote.count("A")
B = vote.count("B")

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")