# 문제 : 알파벳 개수

from string import ascii_lowercase


S = input()
alphabet = list(ascii_lowercase)
alphabet = dict.fromkeys(alphabet, 0)

for i in S:
    alphabet[i] += 1

for j in alphabet:
    print(alphabet[j], end=" ")
