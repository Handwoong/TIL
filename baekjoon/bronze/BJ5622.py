# 문제 : 다이얼
call_number = input()
short_time = 0
dial_number = {
    'ABC': 2,
    'DEF': 3,
    'GHI': 4,
    'JKL': 5,
    'MNO': 6,
    'PQRS': 7,
    'TUV': 8,
    'WXYZ': 9
}

for i in range(len(call_number)):
    for key in dial_number:
        if call_number[i] in key:
            short_time += dial_number[key] + 1
print(short_time)