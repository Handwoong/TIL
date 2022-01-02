# 문제 : 소음

A = input()
op = input()
B = input()

if len(A) < len(B):
    if op == "*":
      print(B+A[1:])
    elif op == "+":
      print(B[:len(B)-len(A)]+A)
elif len(A) > len(B):
    if op == "*":
      print(A+B[1:])
    elif op == "+":
      print(A[:len(A)-len(B)]+B)
else:
    if op == "*":
      print(A+B[1:])
    elif op == "+":
      print("2"+A[1:])