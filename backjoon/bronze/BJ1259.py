# 백준(1259번) : 팰린드롬수
while True:
    s = input()

    if s == '0':
        break
    
    string = []
    for x in s:
        string.append(x)
    
    result = ''
    for i in range(len(string)):
        if string[i] == string[-1-i]:
            result += string[i]
        else:
            result = 'no'
            break
    
    if result == 'no':
        print(result)
    else:
        print('yes')