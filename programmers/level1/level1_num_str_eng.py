# 문제 : 숫자 문자열과 영단어

"""
def solution(s):
    str_num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    answer = ''
    alpha = ''
    for i in s:
        print(i)
        if i.isdigit(): # 숫자라면 True 아니면 False
            answer += i
        else:
            alpha += i
            if alpha in str_num:
                answer += str(str_num[alpha])
                alpha = ''
    return int(answer)
"""

def solution(s):
    str_num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for keys, value in str_num.items():
        s = s.replace(keys, value)
    return int(s)